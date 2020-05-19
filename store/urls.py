from django.urls import path, include
from store import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("products/<catalog>/", views.CatalogProductListView.as_view(), name="catalog_product_list"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("categories/", views.CatalogListView.as_view(), name="catalog_list")
]
