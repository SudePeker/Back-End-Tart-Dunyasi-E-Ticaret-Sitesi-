from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def userGiris(request):
    if 'kayit' in request.POST:
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre = request.POST['sifre']

        if kullanici!='' and email!='' and sifre!='':
            if User.objects.filter(username=kullanici).exists():
                messages.error(request,'Bu kullanıcı adı zaten mevcut')
                return redirect('giris')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Bu email kullanımda')
                return redirect('giris')
            elif len(sifre)<6:
                messages.error(request,'Şifre en az 6 karakter olmalıdır.')
                return redirect('giris')
            elif kullanici.lower() in sifre.lower():
                messages.error(request,'Kullanıcı adı ve şifre benzer olmamalıdır.')
                return redirect('giris')
            else:
                user=User.objects.create_user(username=kullanici,email=email,password=sifre)
                user.save()
                messages.success(request,'Kullanıcı Oluşturuldu.')
                return redirect('anasayfa')
        else:
                messages.error(request,'Tüm alanların doldurulması zorunludur.')
                return redirect('giris')
    if 'giris' in request.POST:
        kullanici=request.POST['kullanici']
        sifre=request.POST['sifre']

        user = authenticate(request, username=kullanici, password=sifre)

        if user is not None:
            login(request,user)
            messages.success(request,'Giriş Yapıldı')
            return redirect('urunler')
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı')
            return redirect('giris')
    return render(request,'giris.html')

def userCikis(request):
    logout(request)
    messages.success(request,'Çıkış Yapıldı')
    return redirect('giris')

def iletisim(request):
    if request.method=='POST':
        ad = request.POST['ad']
        soyad = request.POST['soyad']
        telefon = request.POST['telefon']
        eposta = request.POST['eposta']
        mesaj = request.POST['mesaj']

        if ad!='' and soyad!='' and telefon!='' and eposta!='' and mesaj!='':
            iletisim = Iletisim.objects.create(
                ad = ad,
                soyad = soyad,
                telefon = telefon,
                eposta = eposta,
                mesaj = mesaj
            )
            iletisim.save()
            messages.success(request, 'Mesaj Gönderildi.')
            return redirect('iletisim')
        else:
            messages.error(request,'Tüm alanların doldurulması zorunludur.')
            return redirect('iletisim')
    return render (request,'iletisim.html')

