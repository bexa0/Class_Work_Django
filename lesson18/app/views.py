from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .froms import ProductCreateModelForm, ProductUpdateModelForm
from .models import Product


def product_list_view(request):
    context = {"product_list": Product.objects.all()}
    return render(request, 'app/product_list.html', context)


class ProductListView(ListView):
    template_name = 'app/product_list.html'
    model = Product
    context_object_name = 'product_list'


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, 'app/product_detail.html', context)


class ProductDetailView(DetailView):
    template_name = 'app/product_detail.html'
    model = Product


def product_create_view(request):
    form = ProductCreateModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ProductCreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context['form'] = form
    return render(request, 'app/product_create.html', context)


class ProductCreateView(CreateView):
    template_name = 'app/product_create.html'
    model = Product
    fields = ('name', 'price', 'description', 'quantity')
    success_url = reverse_lazy('product_list')


def product_update_view(request):
    form = ProductCreateModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ProductUpdateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context['form'] = form
    return render(request, 'app/product_update.html', context)


class ProductUpdateView(UpdateView):
    template_name = 'app/product_update.html'
    model = Product
    fields = ('name', 'price', 'description', 'quantity')
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    template_name = 'app/product_delete.html'
    model = Product
    success_url = reverse_lazy('product_list')




