from django.db import models


class ShortenedLink(models.Model):
    original_link = models.URLField()
    short_link = models.CharField(max_length=10, unique=True)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, default="Anonymous")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.name

