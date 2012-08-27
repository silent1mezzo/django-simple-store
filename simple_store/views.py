from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from simple_store.models import Product, Category

def index(request):
    template_name = 'simple_store/base.html'
    context = RequestContext(request)
    dict = {}

    return render_to_response(
        template_name,
        dict,
        context,
    )

def category(request, slug=None):
    template_name = 'simple_store/category.html'
    context = RequestContext(request)
    dict = {}

    category = get_object_or_404(Category, slug=slug)

    return render_to_response(
        template_name,
        dict,
        context,
    )

def product(request, slug):
    template_name = 'simple_store/product.html'
    context = RequestContext(request)
    dict = {}

    return render_to_response(
        template_name,
        dict,
        context,
    )

def cart(request):
    template_name = 'simple_store/cart.html'
    context = RequestContext(request)
    dict = {}

    return render_to_response(
        template_name,
        dict,
        context,
    )
