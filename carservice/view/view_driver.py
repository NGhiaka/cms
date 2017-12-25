from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.contrib import messages
# quan ly tai xe
def driver(request):
    driver_list = Driver.objects.all().order_by('id')
    context = {
        'driver_list': driver_list,
    }
    return render(request, 'carservice/driver/index.html', context)
        
def driver_new(request):
    if request.method == 'POST': 
        f = DriverForm(request.POST)
        od = f.save()
        messages.success(request, "Thêm thành công!!!")
        return redirect('/admin/taixe')
    dF =  DriverForm() 
    return render(request, 'carservice/driver/new.html', {'form':dF})

def driver_detail(request, driver_id):
    try:
        driv = Driver.objects.get(id = driver_id)
    except Driver.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'carservice/driver/show.html', {'driv':driv})
def driver_edit(request, driver_id):
    try:    
        if request.method == 'POST': 
            f = DriverForm(request.POST)
            if f.is_valid(): 
                driv = Driver.objects.get(id=driver_id)
                driv.idcard = f.cleaned_data['idcard']
                driv.drivername = f.cleaned_data['drivername']
                driv.phone_number = f.cleaned_data['phone_number']
                driv.address = f.cleaned_data['address']
                driv.birthday = f.cleaned_data['birthday']
                driv.experience = f.cleaned_data['experience']
                driv.introduce = f.cleaned_data['introduce']
                driv.avatar = f.cleaned_data['avatar']

                driv.save()
          
            return redirect('/admin/taixe/chitiet/'+driver_id)
        driv = Driver.objects.get(id = driver_id)
        dF =  DriverForm() 
        dF.fields['idcard'].initial = driv.idcard
        dF.fields['drivername'].initial = driv.drivername
        dF.fields['phone_number'].initial = driv.phone_number
        dF.fields['address'].initial = driv.address
        dF.fields['birthday'].initial = driv.birthday
        dF.fields['experience'].initial = driv.experience
        dF.fields['introduce'].initial = driv.introduce
        dF.fields['avatar'].initial = driv.avatar


        return render(request, 'carservice/driver/edit.html', {'form':dF})
    except Driver.DoesNotExist:
        raise Http404("Khong tim thay xe")
    return render(request, 'carservice/driver/edit.html', {'driv':driv})

def driver_delete(request, driver_id):
    try:
        d = Driver.objects.get(id = driver_id)
        d.delete()
        return redirect('/admin/taixe/')
    except Driver.DoesNotExist:
        raise Http404("Khong tim thay xe")
# Ket thuc quan ly tai xu