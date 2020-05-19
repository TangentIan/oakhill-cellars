from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from store.models import Product, Catalog


def home(request):
    template = "store/home.html"
    catalog = Catalog.objects.filter(active=True)
    context = {
        "catalog": catalog
    }

    return render(request, template_name=template, context=context)


class CatalogProductListView(ListView):
    context_object_name = "products"
    model = Product

    def get_queryset(self):
        catalog_filter = (
            self.kwargs['catalog'] if 'catalog' in self.kwargs else None
        )
        if catalog_filter:
            self.catalog = get_object_or_404(Catalog, id=self.kwargs['catalog'])
            return Product.objects.filter(catalog=self.catalog)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['catalog'] = self.catalog
        return context


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = "products"


class CatalogListView(ListView):
    queryset = Catalog.objects.filter(active=True)
    context_object_name = "catalogs"
