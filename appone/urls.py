from django.urls import path
from . import views

# urlpatterns for  accounts apps
urlpatterns=[
	path('',views.index, name='index'),

	]