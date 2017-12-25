# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
# from django.contrib import messages
# from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import CarForm
from carservice.models import Car
from django.contrib import messages

# from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView




class CarList(ListView):
    template_name = 'carservice/car/index.html'
    model  = Car

class CarDetail(DetailView):
    template_name = 'carservice/car/show.html'
    model  = Car

class CarCreate(CreateView):
    template_name = 'carservice/car/car_form.html'
    model = Car
    form_class = CarForm
    success_url = '/admin/quanlyxe'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CarUpdate(UpdateView):
    template_name = 'carservice/car/car_form.html'
    form_class = CarForm
    model = Car
    
    success_url = '/admin/quanlyxe'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CarDelete(DeleteView):
    model = Car
    success_url = '/admin/quanlyxe'
    
        



# def car(request):
#     car_list = Car.objects.all().order_by('id')
#     context = {
#         'car_list': car_list,
#     }
#     return render(request, 'carservice/car/index.html', context)
        
# def car_new(request):
#     if request.method == 'POST': 
#         f = CarForm(request.POST)
#         od = f.save()
#         messages.success(request, "Thêm thành công!!!")
#         return redirect('/admin/quanlyxe')
#     cF =  CarForm() 
#     return render(request, 'carservice/car/new.html', {'form':cF})

# def car_detail(request, car_id):
#     try:
#         car = Car.objects.get(id = car_id)
#     except Car.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'carservice/car/show.html', {'car':car})
# def car_edit(request, car_id):
#     try:
        
#         if request.method == 'POST': 
#             f = CarForm(request.POST, request.FILES)
#             if f.is_valid(): 
#                 car = Car.objects.get(id=car_id)
#                 car.carid = f.cleaned_data['carid']
#                 car.nameofcar = f.cleaned_data['nameofcar']
#                 car.manufacturer = f.cleaned_data['manufacturer']
#                 car.owner = f.cleaned_data['owner']
#                 car.typecar = f.cleaned_data['typecar']
#                 car.yearofmanu = f.cleaned_data['yearofmanu']
#                 car.avatar = f.cleaned_data['avatar']
#                 car.save()
#             # to_update = car.update(carid=f.fields['carid'])
#             #messages.success(request, "Cập nhật thành công!!!")
#             # url = reverse('car_detail', args=(), kwargs={'url_id':car.id})
#             return redirect('/admin/quanlyxe/chitiet/'+car_id)
#         car = Car.objects.get(id = car_id)
#         cF =  CarForm() 
#         cF.fields['carid'].initial = car.carid
#         cF.fields['nameofcar'].initial = car.nameofcar
#         cF.fields['manufacturer'].initial = car.manufacturer
#         cF.fields['owner'].initial = car.owner
#         cF.fields['typecar'].initial = car.typecar
#         cF.fields['yearofmanu'].initial = car.yearofmanu
#         cF.fields['avatar'].initial = car.avatar
#         return render(request, 'carservice/car/edit.html', {'form':cF})
#     except Car.DoesNotExist:
#         raise Http404("Khong tim thay xe")
#     return render(request, 'carservice/car/edit.html', {'car':car})

# def car_delete(request, car_id):
#     try:
#         c = Car.objects.get(id = car_id)
#         c.delete()
#         return redirect('../quanlyxe/')
#     except Car.DoesNotExist:
#         raise Http404("Khong tim thay xe")

# # xong phan quan ly xe