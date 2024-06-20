from django.contrib import admin

# Register your models here.
from .models import Post, Comments

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'content', 'create_date']

admin.site.register(Post, PostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'create_date']

admin.site.register(Comments, CommentsAdmin)