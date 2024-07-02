from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from cart.forms import CartAddProductForm


# Create your views here.

def product_list(request, category_slug=None):
    category =None
    categories=Categoria.objects.all()
    products=Producto.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Categoria,
                                 slug=category_slug)
        products=products.filter(category=category)
    return render(request,
                  'shop/producto/list.html',
                  {'category': category,
                   'categories':categories,
                   'products':products})

def product_detail(request, id, slug):
    product=get_object_or_404(Producto,
                            id=id,
                            slug=slug,
                            available=True)
    cart_product_form=CartAddProductForm()
    return render(request,
                  'shop/producto/detail.html',
                  {'product':product,
                   'cart_product_form':cart_product_form})


