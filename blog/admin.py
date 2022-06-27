from django.contrib import admin
from blog.models import Category, Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_display = ['title', 'author', 'counted_views', 'status', 'published_date']
    list_filter = ['status','author',]
    ordering = ['-created_date']



class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved')
    list_filter = ('post', 'approved')
    search_fields = ('name', 'post')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
