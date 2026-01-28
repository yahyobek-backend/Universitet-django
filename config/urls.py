"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page_view, name='home'),
    path('directions/',directions_view, name='directions'),
    path('directions/<int:pk>/', direction_view, name='direction-details'),
    path('subjects/',subjects_view, name='subjects'),
    path('subjects/<int:pk>/', subject_view, name='subject-details'),
    path('teachers/',teachers_view, name='teachers'),
    path('teachers/<int:pk>/', teacher_view, name='teacher-details'),
]
