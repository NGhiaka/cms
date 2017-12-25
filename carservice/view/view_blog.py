# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
# from django.contrib import messages
# from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import BlogForm
from carservice.models import Blog
from django.contrib import messages

# from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView




class BlogList(ListView):
    template_name = 'carservice/blog/index.html'
    model  = Blog

class BlogDetail(DetailView):
    template_name = 'carservice/blog/show.html'
    model  = Blog

class BlogCreate(CreateView):
    template_name = 'carservice/blog/form.html'
    model = Blog
    form_class = BlogForm
    success_url = '/admin/blog'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class BlogUpdate(UpdateView):
    template_name = 'carservice/blog/form.html'
    form_class = BlogForm
    model = Blog
    
    success_url = '/admin/blog'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class BlogDelete(DeleteView):
    model = Blog
    success_url = '/admin/blog'
    
        
