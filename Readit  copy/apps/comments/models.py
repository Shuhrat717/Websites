from django.db import models


class Comments(models.Model):
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='comments/', null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

