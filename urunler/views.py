from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request, 'anasayfa.html')


def urunler(request):
    kategoriler = Kategori.objects.all()
    urunler = Urun.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains=search) |
            Q(kategori__isim__icontains=search) |
            Q(sub_category__isim__icontains=search)
        )
    context = {
        'kategoriler': kategoriler,
        'urunler': urunler,
        'search': search
    }

    return render(request, 'urunler.html', context)


def iletisim(request):
    return render(request, 'iletisim.html')


def sepet(request):
    return render(request, 'sepet.html')


def giris(request):
    return render(request, 'giris.html')


def view_404(request, exception):
    return redirect('/')
