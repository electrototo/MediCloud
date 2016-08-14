from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'', views.loginToPage, name='login'),
	url(r'logout/', views.logoutUser, name='logout')
]