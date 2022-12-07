from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=100)
    month = models.IntegerField(default=3)
    day = models.IntegerField(default=3)
    price = models.IntegerField(default=0)
    desc = models.TextField()
    idx = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






