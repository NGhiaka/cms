from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
# from django_ajax.decorators import ajax
# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from django.contrib.auth import login, authenticate
# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.views.generic import ListView, TemplateView
# from django.contrib import messages
from django.utils.timezone import datetime
# from passlib.hash import pbkdf2_sha256

# class indexList(ListView):
#     template_name = 'carservice/page/index.html'
#     model  = Schedule


def index(request):
    today = datetime.today()
    schs = Schedule.objects.all()
    forms = []
    schedule = Schedule.objects.filter(departure_day__lte = today, destination_day__gte = today)
    context = {}
    for sch in schs:
        # form = ScheduleForm(instance = sch)
        forms.append({'title':sch.guess_name,'start':sch.departure_day.strftime('%Y-%m-%d'),'end': sch.destination_day.strftime('%Y-%m-%d')})
        context = {
            'schedules':schedule, 
            'forms': forms,
        }

    return render(request, 'carservice/page/index.html', context)

def statistical_car(request):
    return render(request, 'carservice/page/statistical_car.html')

def statistical_income(request):
    return render(request, 'carservice/page/statistical_income.html')



# def schedule_json(request):
#     data_list = []
#     data_json = {}
#     # if request.is_ajax():
#     #     if request.method == 'POST':
#     schedule_list = Schedule.objects.all()        
#     if schedule_list:
#         for sch in schedule_list:
#             data = {
#                 'date': sch.departure_day,
#                 "badge":True,
#                 "title":"Tonight",
#                 'body': sch.guess_name,
#                 "footer":"At Paisley Park",
#                 "classname":"purple-event"
#             }
#             data_list.append(data)

#     data_json['key'] = data_list
#     # d = serializers.serialize('json', data_json)

    # return data_list
    # return JsonResponse(data_list, safe=False)  #


def login(request):
    error_message = ''
    if request.method == 'POST': 
        form = UserLoginForm(request.POST)
        if form.is_valid():
            us = form.fields['username']
            password = form.fields['password']
            enc_pass = pbkdf2_sha256.encrypt(form.fields['password'], rounds=12000, salt_size=32) 
            user = User.objects.filter(username = us)
            # isPass = pbkdf2_sha256.verify(password, user.clear_data['password'])
            isPass = pbkdf2_sha256.verify(user.fields['password'], enc_pass)
            # user.sjha
            if user:

                # login(request, user)
                return redirect('admin/')
            else:
                error_message = 'Tên đăng nhập hoặc mật khẩu không đúng!!!'
    loginForm = UserLoginForm() 
    return render(request, 'carservice/login/login.html', {'form': loginForm, 'error_message': error_message})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['fullname']:
                error_message = 'Vui lòng nhập họ tên!!'
            elif User.objects.filter(username=form.cleaned_data['username']).exists():
                error_message = 'Tài khoản đã được tạo'
            elif form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                error_message = 'Mật khẩu nhập lại không khớp!!!'
            else:
                enc_pass = pbkdf2_sha256.encrypt(form.cleaned_data['password'], rounds=12000, salt_size=32) 
                form.fields['password'].initial = enc_pass
                # form.sdsd
                form.save()
                return redirect(LOGIN_REDIRECT_URL)
    registerForm = UserRegisterForm() 
    return render(request, 'carservice/login/signup.html', {'form': registerForm, 'error_message': error_message})