from django.contrib import admin
from store.models import Product, Catalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "catalog", "slug", "price")
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ("catalog",)


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
