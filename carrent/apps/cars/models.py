from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/")
    fee = models.IntegerField()
    doors = models.IntegerField()
    seats = models.IntegerField()
    tr = models.CharField(max_length=200)
    age = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

