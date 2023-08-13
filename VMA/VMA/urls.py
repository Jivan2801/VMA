"""
URL configuration for VMA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import *

urlpatterns = [
    path('' , home , name='home'),
    path('add-vehicle/' , add_vehicle , name='add_vehicle'),
    path('delete-vehicle/<id>/', delete_vehicle, name="delete_vehicle"),
    path('update-vehicle/<id>/', update_vehicle, name="update_vehicle"),
    path('log_in/' , log_in , name='log_in'),
    # path('Vehicle-view/',Vechileview, name= Vechileview),
    path('register/' , register , name='register'),
    path('log_out/' , log_out , name='log_out'),
    path('Vechile-view/' , Vechileview , name='Vechileview'),
    path('admin/', admin.site.urls),
]
