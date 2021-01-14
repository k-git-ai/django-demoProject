from django.urls import path
from . import views

# urlpatterns for  accounts apps
urlpatterns=[
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('profile', views.profile, name='profile'),

	]