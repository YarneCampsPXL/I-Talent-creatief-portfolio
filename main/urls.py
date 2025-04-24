from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='over mij'),
    path('innovatie/', views.innovatie, name='innovatie'),
    path('seminaries/', views.seminaries, name='seminaries'),
    path('persoonlijke_ontwikkeling/', views.persoonlijke_ontwikkeling, name='persoonlijke ontwikkeling'),
    path('internationalisering/', views.internationalisering, name='internationalisering'),
    path('selectie/', views.selectie, name='selectie'),
    path('eindreflectie/', views.eindrelfectie, name='eindreflectie'),
]
