from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, Category
from .forms import ProductForm

def product_upload(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('gallery')
    return render(request, 'products/upload.html', {'form': form})

def product_gallery(request):
    categories = Category.objects.all()
    selected = request.GET.get('category')
    query = request.GET.get('q', '')

    products = Product.objects.all()
    if selected:
        products = products.filter(category__name=selected)
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)

    return render(request, 'products/gallery.html', {
        'products': products,
        'categories': categories,
        'selected': selected,
        'query': query,
    })

def export_json(request):
    products = Product.objects.all().values('name', 'description', 'price', 'category__name')
    return JsonResponse(list(products), safe=False)