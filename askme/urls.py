"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('templates/add_question.html', views.add_question),
     path('', views.index),
     path('index.html', views.index),
     path('templates/index.html', views.index),
     path('templates/registration.html', views.registration),
     path('templates/log_in.html', views.log_in),
     path('templates/profile.html', views.profile),
     path('templates/question_by_tag.html', views.question_by_tag),
     path('templates/answer.html', views.answer),
]
