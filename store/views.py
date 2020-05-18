from django.shortcuts import render
from django.views.generic import ListView

from store.models import Product


def home(request):
    template = "store/home.html"

    return render(request, template_name=template)


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = "products"
