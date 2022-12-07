from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    content = RichTextField()
    tags = models.ManyToManyField(Tags)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to="media/")
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    title = models.CharField(max_length=221)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@property
def get_image_url(self):
    if settings.DEBUG:
        return f'http://127:0.0.1:8000{self.image.url}'
    return f'http://127:0.0.1:8000{self.image.url}'
