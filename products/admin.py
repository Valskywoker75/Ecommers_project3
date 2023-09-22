from django.contrib import admin
from .models import Category, Product, ProductImage, Comment, User

admin.site.register(Category)
admin.site.register(User)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    inlines = [ProductImageInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at', 'product']
    list_filter = ['created_at']
    search_fields = ['text']
    readonly_fields = ['created_at']
