from django.urls import path, include
from store import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("products/", views.ProductListView.as_view(), name="product_list")
]
