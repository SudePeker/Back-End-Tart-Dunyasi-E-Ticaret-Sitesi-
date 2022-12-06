from django.urls import path
from .views import *
urlpatterns = [
    path('giris/',userGiris,name='giris'),
    path('cikis/',userCikis,name='cikis'),
    path('iletisim/',iletisim,name='iletisim')
]
