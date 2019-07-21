from django.contrib import admin
from accounts.models import Post, Comment

# Register your models here.\

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish','status',  )
    search_fields= ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
   # list_filter =
    list_filter = ('status', 'created', 'publish')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active', 'created')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'updated')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)