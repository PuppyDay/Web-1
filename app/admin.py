from django.contrib import admin
from app import models

admin.site.register(models.Author)
admin.site.register(models.Article)
admin.site.register(models.Tag)
admin.site.register(models.LikeDislike)
admin.site.register(models.Answer)


