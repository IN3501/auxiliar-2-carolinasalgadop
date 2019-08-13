from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('equipoDocente/', views.equipoDocente, name='equipoDocente'),
	path('libre/', views.libre, name='libre'),
]