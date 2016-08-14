from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^dashboard/', views.dashboard, name="dash"),
	url(r'^dispositives/', views.dispositives, name="dispositives"),
	url(r'^doctors/', views.doctors, name="doctors"),
	url(r'^family/', views.family, name="family"),
	url(r'^medicine/', views.medicine, name="medicine"),
	url(r'^account/', views.account, name="account"),

	url(r'^statistics/', views.statistics, name="statistics"),
	url(r'^patients/', views.patients, name="patients"),
	url(r'^profileDoc/', views.accountDoctor, name="doctorAccount")
]