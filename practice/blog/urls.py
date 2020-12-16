from django.urls import path,include
from . import views

urlpatterns = [
	path( '', views.post_list, name='post' ),
	path( 'create/', views.post_create, name='create' ),
	path( 'update/<int:pk>/', views.post_update, name='update' ),
	path( 'delete/<int:pk>/', views.post_delete, name='delete' )
]