from django.contrib import admin

from .models import Category, Product, Image


admin.site.register(Category)


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]