from django.contrib import admin
from .models import Artwork, Like, Comment


class Like_Admin(admin.ModelAdmin):
    list_display = ('user', 'artwork')


class Artwork_Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_created', 'status', 'picture')


admin.site.register(Artwork, Artwork_Admin)
admin.site.register(Like, Like_Admin)
admin.site.register(Comment)

