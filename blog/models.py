from django.db import models
from core.models import TimeStampedModel


def blog_thumbnail_upload(instance, filename):
    return f"blog/thumbnails/{filename}"


class Category(TimeStampedModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=blog_thumbnail_upload, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts"
    )
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField()  # بعداً User FK می‌شود

    def __str__(self):
        return self.title
