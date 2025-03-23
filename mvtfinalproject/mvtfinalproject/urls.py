"""
URL configuration for mvtfinalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from testapp import views


urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    path('',views.homeview),
    path('allstudents/',views.allstudentslistview.as_view()),
    path('pythonstudents/',views.pythonview),
    path('djangostudents/',views.djangoview),
    path('adminstudents/',views.adminlistview.as_view(),name="adminstudents"),
    path('create/',views.admincreateview.as_view()),
    path('update/<int:pk>',views.adminupdateview.as_view()),
    path('delete/<int:pk>',views.admindeleteview.as_view()),
    path('logout/',views.logoutview),
    path('signup/',views.signupview)

]
