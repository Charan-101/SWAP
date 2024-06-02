
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name="home"),
    path('collections',views.collections,name="collections"),
    path('login',views.loginn,name="login"),
    path('register',views.register,name="register"),
    path('productview', views.product_view, name='productview'),

]
