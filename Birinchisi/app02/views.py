from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import *
def salom(request):
    data={
        'kitob': Muallif.objects.all()
    }
    return render(request, 'index.html', data)
def kitob(request):
    data={
        'kitob': Kitob.objects.all()
    }
    return render(request, 'kitob.html', data)
def muallif(request):
    data={
        'kitob': Muallif.objects.all()
    }
    return render(request, 'muallif.html', data)
def record(request):
    data={
        'kitob': Kutubxona.objects.all()
    }
    return render(request, 'record.html', data)
def bitta_muallif(request, son):
    data={
        'kitob': Muallif.objects.get(id=son)
    }
    return render(request, 'bitta_mualif.html', data)
def muallif_true(request):
    data={
        'kitob': Muallif.objects.filter(trik='True')
    }
    return render(request, 'muallif_true.html', data)


def Muallif(request):
    qidiruv= request.GET.get('qidir')
    xammasi=Muallif.objects.all()
    if qidiruv:
        xammasi = Muallif.objects.filter(ism__contains=qidiruv)
    data={
        'M'
        ''
        'uallif': xammasi
    }
    return render(request, 'muallif.html', data)

def ochir(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect("/Muallif/")
