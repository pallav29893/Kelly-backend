from django.contrib import admin
from .models import Post
# from django.contrib.auth.admin import UserAdmin
from .models import Category,Comment,Tag

# admin.site.register(User)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "published_date")
    search_fields = ['author','category','tags']
    autocomplete_fields = ['category','tags']

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    # prepopulated_fields = {"slug": ["name",]}
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display =('name','slug')
    # prepopulated_fields = {"slug": ["name",]}
    search_fields = ['name']

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)

