"""
URL configuration for crudempleados project.

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
from empleados import views
from django.conf.urls.static import static

app_name = 'empleados'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('social_security',
         views.social_security,
         name="ss"),
    path('social_security/<int:ss_pk>',
         views.social_security_detail,
         name="ss_detail"),
    path('social_security/<int:ss_pk>/delete',
         views.social_security_delete,
         name="ss_delete"),
    path('social_security/<int:ss_pk>/update',
         views.social_security_update,
         name="ss_update"),
    path('employee/<int:employee_pk>',
         views.employee_detail,
         name="employee_detail"),
    path('employee/<int:employee_pk>/delete',
         views.employee_delete,
         name="employee_delete"),
    path('employee/<int:employee_pk>/update',
         views.employee_update,
         name="employee_update"),
    path('employees/create',
         views.employee_creation,
         name="employee_creation"),
    path('social_security/create',
         views.social_security_creation,
         name="social_security_creation"),
]
