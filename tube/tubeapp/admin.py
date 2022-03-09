from django.contrib import admin

from .models import Mijoz, Playlist, Video, Comment
admin.site.register(Mijoz)
admin.site.register(Playlist)
admin.site.register(Video)
admin.site.register(Comment)