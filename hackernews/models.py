from django.db import models
import uuid


class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.PositiveIntegerField(null=True)
    author = models.CharField(max_length=200)
    descendants = models.PositiveIntegerField(null=True)
    score = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.URLField(max_length=2000, null=True)
    time = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["time"]
        verbose_name_plural = "Stories"


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.PositiveIntegerField(null=True)
    author = models.CharField(max_length=255, null=True)
    parent = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(null=True)
    time = models.PositiveBigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["time"]
        verbose_name_plural = "Comments"
