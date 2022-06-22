from django.contrib import admin

# Register your models here.
# a new import
from blogging.models import Post, Category

class CategoryInline(admin.StackedInline):
    model = Category.posts.through

# and a new admin registration
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

