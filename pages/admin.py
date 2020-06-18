from django.contrib import admin
from .models import BlogPost


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    search_fields = ('title','content','author')
    list_per_page = 25


admin.site.register(BlogPost, BlogPostAdmin)
