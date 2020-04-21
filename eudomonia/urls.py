from django.contrib import admin
from django.urls import path,include
from . import views

 
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('communicable/', views.communicable),
    path('noncommunicable/', views.noncommunicable),
    path('accounts/', include('accounts.urls')),
    
]