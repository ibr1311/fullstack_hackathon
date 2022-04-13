from django.contrib import admin
from main.models import Type, Product, ProductImage


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = [
    'slug', 'name'
    ]
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 10
    min_num = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]