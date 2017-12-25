# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
# from django.contrib import messages
# from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import CustomerForm
from carservice.models import Customer
from django.contrib import messages

# from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView




class CustomerList(ListView):
    template_name = 'carservice/customer/index.html'
    model  = Customer

class CustomerDetail(DetailView):
    template_name = 'carservice/customer/show.html'
    model  = Customer

class CustomerCreate(CreateView):
    template_name = 'carservice/customer/form.html'
    model = Customer
    form_class = CustomerForm
    success_url = '/admin/quanlyxe'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CustomerUpdate(UpdateView):
    template_name = 'carservice/customer/form.html'
    form_class = CustomerForm
    model = Customer
    
    success_url = '/admin/khachhang'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CustomerDelete(DeleteView):
    model = Customer
    success_url = '/admin/khachhang'
    