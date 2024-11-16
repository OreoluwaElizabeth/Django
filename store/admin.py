from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product
from .models import Collection


# Register your models here.

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'price', 'description', 'inventory_status', 'collection']
    list_per_page = 10
    list_editable = ['price', 'description']
    search_fields = ['name']

    @admin.display(ordering='-inventory')
    def inventory_status(self, product: Product):
        if product.inventory < 20:
            return 'Low'
        return 'High'

@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ['id', 'name', 'product_count']
    list_per_page = 20

    def product_count(self, collection):
       return collection.product_set.count()