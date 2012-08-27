from django.contrib import admin
from simple_store.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'active')
    prepopulated_fields = {"slug": ("name", )}
    list_filter = ('active', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
