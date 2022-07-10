from django.contrib import admin

from .models import Category, Product, Rating


admin.site.register(Category)


class RatingInline(admin.StackedInline):
    model = Rating
    extra = 0
    classes = ['collapse']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [RatingInline]
