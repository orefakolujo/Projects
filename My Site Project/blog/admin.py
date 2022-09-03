from django.contrib import admin
from .models import Author, Tag, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("title",)}
    list_display = ("title", "author", "date")
    list_filter= ("author", "tag", "date")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
