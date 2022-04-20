from django.contrib import admin
from main.models import Type, Product, Comment

admin.site.register(Product)
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = [
    'slug', 'name'
    ]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Comment)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImageInline, ]