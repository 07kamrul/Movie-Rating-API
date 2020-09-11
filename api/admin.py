from django.contrib import admin
from .models import *

#Django Admin GUI

@admin.register(UserInfo)
class UserInfo(admin.ModelAdmin):
    list_display = ['name','phone','password','email']

@admin.register(Movie)
class Movie(admin.ModelAdmin):
    list_display = ['name','release_date']
    list_filter = ['release_date','rating']
    search_fields = ['name']


@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display = ['user_id','movie_id','rating']
    list_filter = ['rating']
