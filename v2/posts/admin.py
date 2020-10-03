from django.contrib import admin
from .models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=("user",)
class PostAdmin(admin.ModelAdmin):
    list_display=("title","author")
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
