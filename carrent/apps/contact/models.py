from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name




