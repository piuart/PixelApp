from page.models import Category, Post
from django.contrib import admin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


admin.site.register(Category)
admin.site.register(Post,PostAdmin)