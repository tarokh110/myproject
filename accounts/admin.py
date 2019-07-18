from django.contrib import admin
from accounts.models import user,Post

# Register your models here.\
"""
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display =('price','votes','feature')
   fieldsets = (
        (None, {
            'fields': ('votes')
        }),
        ('Availability', {
            'fields': ('price')
        }),
    )
"""

admin.site.register(user)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish','status' )
    search_fields= ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
   # list_filter =
    list_filter = ('status', 'created', 'publish')


admin.site.register(Post, PostAdmin)


class useradmin(admin.ModelAdmin):
    list_filter = ('s')