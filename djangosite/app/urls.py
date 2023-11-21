from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='Home'),  
    path('Home',views.index,name='Home'),  
    path('about',views.about,name='about'),


]

