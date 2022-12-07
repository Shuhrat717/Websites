from django.db import models
from apps.cars.models import Cars


class Team(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="media/")
    content = models.TextField()
    position = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/")
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class History(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/")
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Trip(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='trips')
    where_from = models.CharField(max_length=221)
    where_go = models.CharField(max_length=221)
    journey_date = models.DateField()
    return_date = models.DateField()
