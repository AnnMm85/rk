from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, CreateView

from .forms import RegisterForm, SearchForm
from .models import *


class IndexView(generic.ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.GET.get('search_query')

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'main/index.html')


@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    date_d = Basket.objects.create(user=user, product=product)
    return HttpResponseRedirect('/')


class RegisterView(CreateView):
    model = CustUser
    template_name = 'main/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('main:login')


class ProductListView(generic.ListView):
    model = Product
    template_name = 'main/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.GET.get('search_query')

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Basket
    template_name = 'main/profile.html'
    context_object_name = 'baskets'
