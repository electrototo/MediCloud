from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.sendmail, name='login'),
	url(r'^getAlarm/', views.getAlarm, name='getAlarm'),
]