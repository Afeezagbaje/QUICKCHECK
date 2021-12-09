from django_filters.rest_framework import FilterSet
import django_filters
from .models import Story


class StoryFilter(FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Story
        fields = ["author", "created_at", "type"]
