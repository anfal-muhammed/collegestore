from django.conf import settings
from django.contrib import admin
from django.urls import path
from.import views
from django.urls import path
from . import views
app_name = 'collegeapp'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('register',views.register,name='register'),
    path('login', views.login_view, name='login_view'),
    path('new_page',views.new_page,name='new_page'),
    path('order_form/',views.order_form,name='order_form'),
    path('ajax/load-courses/',views.load_courses,name='ajax_load_courses'),
]