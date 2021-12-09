from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from utils.hackernews_api import HackerNewsApi
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from hackernews.models import Story
from hackernews.pagination import DefaultPagination
from hackernews.serializers import StorySerializer
from hackernews.filter import StoryFilter


class ReadStoryViewset(ReadOnlyModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    hackernews_api = HackerNewsApi("topstories")
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StoryFilter
    error = "Not allowed"
    lookup_field = "id"

    def save_item_data(self):
        create_item = []
        res = self.hackernews_api.get_all_stories()
        try:
            for story in res[:10]:
                print(story)
                res_story = self.hackernews_api.get_a_story(story)
                create_item = Story.objects.get_or_create(
                    author=res_story["by"],
                    descendants=res_story["descendants"],
                    score=res_story["score"],
                    title=res_story["title"],
                    url=res_story["url"],
                    time=res_story["time"],
                    item_id=res_story["id"],
                    type=res_story["type"],
                    created_at=res_story["created"],
                )
                print("create item", create_item)
                create_item.save()
            serializer = StorySerializer(create_item)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(err)

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            data = self.queryset.get(pk=kwargs.get("pk"))
            serializer = StorySerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(
                {"detail": "Item field cannot be blank"},
                status.HTTP_400_BAD_REQUEST,
            )
        except Exception as err:
            return Response(
                {"detail": err},
                status.HTTP_404_NOT_FOUND,
            )


class WriteStoryViewSet(ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = StorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def list(self, request):
        queryset = Story.objects.all()
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            story = Story.objects.get(pk=pk)
            serializer = StorySerializer(story)
            return Response(serializer.data, status.HTTP_200_OK)
        except Story.DoesNotExist:
            return Response(
                {"detail": "Item not found"}, status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            id = self.kwargs.get("pk")
            story = Story.objects.filter(pk=id).values("item_id")
            itemId = list(story)[0].get("item_id")
            data = self.queryset.get(pk=kwargs.get("pk"))
            if itemId:
                return Response({"errors": "Not allowed"}, status.HTTP_401_UNAUTHORIZED)
            serializer = StorySerializer(
                data, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(
                {"detail": "Item field cannot be blank"},
                status.HTTP_400_BAD_REQUEST,
            )
        except Exception:
            return Response(
                {"detail": "Item not found"},
                status.HTTP_404_NOT_FOUND,
            )

    def destroy(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        story = Story.objects.filter(pk=id).values("item_id")
        itemId = list(story)[0].get("item_id")
        if itemId:
            return Response({"errors": "not allowed"}, status.HTTP_401_UNAUTHORIZED)
        item = self.get_object()
        item.delete()
        item.save()
        return Response({"data": "delete success"},  status.HTTP_204_NO_CONTENT)
