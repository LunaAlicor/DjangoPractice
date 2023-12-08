from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, OrderForm
from .models import Product, Orders


class IndexView(View):
    def get(self, request):
        return render(request, 'shopaap/index.html')


def shop(request):
    return render(request, 'shopaap/shop.html')


def group_list(request):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopaap/group-list.html', context=context)


# class ProductListView(TemplateView):
#     template_name = 'shopaap/product-list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.all()
#         return context
class ProductListView(ListView):
    template_name = 'shopaap/product-list.html'
    model = Product
    context_object_name = 'products'


# def product_list(request):
#     context = {
#         "products": Product.objects.all(),
#     }
#     return render(request, 'shopaap/product-list.html', context=context)


def order_list(request):
    context = {
        'orders': Orders.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopaap/order-list.html', context=context)


class ProductCreateView(CreateView):
    model = Product
    fields = 'name', 'description', 'price', 'discount'
    template_name = 'shopaap/create_product.html'
    success_url = reverse_lazy('products')
    # Если хотим указать форму то можно использовать form_class


class ProductUpdateView(UpdateView):
    model = Product
    fields = 'name', 'description', 'price', 'discount'

    def get_success_url(self):
        return reverse(
            'product_detail',
            kwargs={'pk': self.object.pk}
        )

# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#
#         if form.is_valid():
#             new_product = form.save(commit=False)
#             new_product.save()
#             return redirect('products')
#
#     else:
#         form = ProductForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'shopaap/create_product.html', context)


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

    else:
        form = OrderForm()

    context = {
        "form": form
    }
    return render(request, 'shopaap/create_order.html', context=context)


# class ProductDitailsView(View):
#     def get(self, request, product_id):
#         product = Product.objects.get(pk=product_id)
#         context = {
#             "product": product
#         }
#         return render(request, 'shopaap/product_detai.html', context=context)

class ProductDitailsView(DetailView):
    template_name = 'shopaap/product_detai.html'
    model = Product  # можно указать кверисет
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')


# class ProductSoftDeleteView(DeleteView):
#     model = Product
#     success_url = reverse_lazy('products')
#
#     def form_valid(self, form):
#         success_url = self.get_success_url()
#         self.object.archived = True
#         self.object.save()
#         return HttpResponseRedirect(success_url)
