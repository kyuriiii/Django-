from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('main/', views.main, name='main'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
]