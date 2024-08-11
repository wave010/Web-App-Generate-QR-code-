from django.urls import path
from QRcodeApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate-qr', views.generateQR, name='generateQR')
]