from django.contrib import admin
from .models import Category, Product
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, AdminCategory)

class AdminProduct(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug',
                    'description', 'price', 'stock',
                    'available', 'created', 'updated', 'image']
    prepopulated_fields =  {'slug': ('name',)}
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']

admin.site.register(Product, AdminProduct)
