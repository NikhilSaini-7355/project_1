from django.urls import path
from django.shortcuts import render
from . import views
urlpatterns = [
    path('pictures/',views.index,name = 'index'),
    path('pictures/<int:cate>/',views.criteria,name='category'),
    path('pictures/phrase/',views.phrase,name='text'),
    path('pictures/miscellaneous/',views.miscel1,name='miscel1'),
    path('pictures/miscellaneous/forms',views.miscel,name='miscel'),
    path('pictures/hear/',views.hear,name = 'hear'),

    
]