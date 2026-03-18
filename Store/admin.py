from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Product 


class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'category', 'price', 'stock', 'is_active', 'created_at') 
    search_fields = ('name',) 
    list_filter = ('category', 'is_active') 
    prepopulated_fields = {'slug': ('name',)} 
    filter_horizontal = ('tags',) 


admin.site.register(Category) 
admin.site.register(Tag) 
admin.site.register(Product, ProductAdmin)
