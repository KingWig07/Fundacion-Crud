"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mandatos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('mandatos/', views.mandatos, name='mandatos'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('mandatos/crear/', views.crear_mandato, name='crear_mandato'),
    path('mandatos/<int:mandato_id>/', views.mandato_detalle, name='mandato_detalle'),
    path('mandatos/eliminar/<int:mandato_id>/', views.eliminar_mandato, name='eliminar_mandato'),
]
