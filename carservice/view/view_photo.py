from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.contrib import messages

# quan ly anh
def album(request):
    album_list = Album.objects.all().order_by('id')
    context = {
        'album_list': album_list,
    }
    return render(request, 'carservice/album/index.html', context)
        
def album_new(request):
    if request.method == 'POST': 
        f = AlbumForm(request.POST)
        if f.is_valid():
            od = f.save()
            # album =  Album.objects.get(title = f.cleaned_data['title'])
            return redirect('/admin/anh/them/'+ str(od.id).strip())
    dF =  AlbumForm() 
    return render(request, 'carservice/album/new.html', {'form':dF})

def album_detail(request, album_id):
    try:
        photo_list = Photo.objects.filter(album = album_id)
        album = Album.objects.get(id  = album_id)
        context = {
            'photo_list': photo_list,
            'album_name' : album,
        }
        return render(request, 'carservice/album/show.html', context)
    except Album.DoesNotExist:
        raise Http404("Question does not exist")
    # return render(request, 'carservice/album/show.html', {'al':al})
def album_edit(request, album_id):
    try:    
        if request.method == 'POST': 
            f = AlbumForm(request.POST)
            if f.is_valid(): 
                al = Album.objects.get(id=album_id)
                al.title = f.cleaned_data['title']
                al.decription = f.cleaned_data['decription']
                al.save()
          
            return redirect('/admin/album/chitiet/'+album_id)
        al = Album.objects.get(id = album_id)
        dF =  AlbumForm() 
        dF.fields['title'].initial = al.title
        dF.fields['decription'].initial = al.decription
        
        return render(request, 'carservice/album/edit.html', {'form':dF})
    except Album.DoesNotExist:
        raise Http404("Khong tim thay xe")
    return render(request, 'carservice/album/edit.html', {'driv':driv})

def album_delete(request, album_id):
    try:
        d = Album.objects.get(id = album_id)
        p = Photo.objects.filter(album = album_id)
        d.delete()
        p.delete()
        return redirect('/admin/album/')
    except Album.DoesNotExist:
        raise Http404("Khong tim thay album")


def photo(request):
    photo_list = Photo.objects.all().order_by('id')
    context = {
        'photo_list': photo_list,
    }
    return render(request, 'carservice/photo/index.html', context)
        
def photo_new(request, album_id):
    if request.method == 'POST': 
        f = PhotoForm(request.POST, request.FILES)
        if f.is_valid():
            photo= Photo()
            photo.album = album_id
            photo.path_img = f.cleaned_data["path_img"]
            photo.comment_img = f.cleaned_data["comment_img"]
            photo.save()
        messages.success(request, "Thêm thành công!!!")
        return redirect('/admin/album/chitiet/'+ album_id)
    dF =  PhotoForm() 
    # dF.fields['album'].initial = album_id
    return render(request, 'carservice/photo/new.html', {'form':dF})

def photo_detail(request, photo_id):
    try:
        al = Photo.objects.get(id = photo_id)
    except Photo.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'carservice/photo/show.html', {'al':al})
def photo_edit(request, photo_id):
    try:    
        if request.method == 'POST': 
            f = PhotoForm(request.POST, request.FILES)
            if f.is_valid(): 
                al = Photo.objects.get(id=photo_id)
                al.album = f.cleaned_data['album']
                al.path_img = f.cleaned_data['path_img']
                al.comment_img = f.cleaned_data['comment_img']
                al.save()
          
            return redirect('/admin/anh/chitiet/'+photo_id)
        al = Photo.objects.get(id = photo_id)
        dF =  PhotoForm() 
        dF.fields['album'].initial = al.album
        dF.fields['path_img'].initial = al.path_img
        dF.fields['comment_img'].initial = al.comment_img
        
        return render(request, 'carservice/photo/edit.html', {'form':dF})
    except Photo.DoesNotExist:
        raise Http404("Khong tim thay anh")
    return render(request, 'carservice/photo/edit.html', {'driv':driv})

def photo_delete(request, photo_id):
    try:
        d = Photo.objects.get(id=photo_id)
        album_id =  d.album.id
        d.delete()
        return redirect('/admin/album/chitiet/' + str(album_id).strip())
    except Photo.DoesNotExist:
        raise Http404("Khong tim thay photo")