from django.contrib import admin
from .models import ShortenedLink, Comment

admin.site.register(ShortenedLink)
admin.site.register(Comment)
