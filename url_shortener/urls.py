
from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('stats/<str:code>/', views.stats, name='stats'),
    path('<str:code>/', views.redirect_url, name='redirect_url'),
]
