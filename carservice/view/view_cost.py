from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.contrib import messages

def cost(request):
    cost_list = Cost.objects.all().order_by('id')
    context = {
        'cost_list': cost_list,
    }
    return render(request, 'carservice/cost/index.html', context)
        
def cost_new(request):
    if request.method == 'POST': 
        f = CostForm(request.POST)
        od = f.save()
        messages.success(request, "Thêm thành công!!!")
        return redirect('/admin/quanlyxe')
    cF =  CostForm() 
    return render(request, 'carservice/cost/new.html', {'form':cF})

def cost_detail(request, cost_id):
    try:
        cost = Cost.objects.get(id = cost_id)
        total_cost = cost.total_revenue - cost.spent_oil - cost.spent_steersman - cost.spent_arises
    except Cost.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'carservice/cost/show.html', {'cost':cost, 'total_cost': total_cost})
def cost_edit(request, cost_id):
    try:
        
        if request.method == 'POST': 
            f = CostForm(request.POST)
            if f.is_valid(): 
                cost = Cost.objects.get(id=cost_id)
                cost.schedule = f.cleaned_data['schedule']
                cost.total_revenue = f.cleaned_data['total_revenue']
                cost.spent_oil = f.cleaned_data['spent_oil']
                cost.spent_steersman = f.cleaned_data['spent_steersman']
                cost.spent_arises = f.cleaned_data['spent_arises']
                cost.save()
            # to_update = Cost.update(costid=f.fields['costid'])
            #messages.success(request, "Cập nhật thành công!!!")
            # url = reverse('cost_detail', args=(), kwargs={'url_id':Cost.id})
            return redirect('/admin/quanlyxe/chitiet/'+cost_id)
        cost = Cost.objects.get(id = cost_id)
        cF =  CostForm() 
        cF.fields['schedule'].initial = cost.schedule
        cF.fields['total_revenue'].initial = cost.total_revenue
        cF.fields['spent_oil'].initial = cost.spent_oil
        cF.fields['spent_steersman'].initial = cost.spent_steersman
        cF.fields['spent_arises'].initial = cost.spent_arises
        
        return render(request, 'carservice/cost/edit.html', {'form':cF})
    except Cost.DoesNotExist:
        raise Http404("Khong tim thay xe")
    return render(request, 'carservice/cost/edit.html', {'cost':cost})

def cost_delete(request, cost_id):
    try:
        c = Cost.objects.get(id = cost_id)
        c.delete()
        return redirect('../quanlyxe/')
    except Cost.DoesNotExist:
        raise Http404("Khong tim thay xe")

# xong phan quan ly xe
# quan ly tai xe