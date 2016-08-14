from django.shortcuts import render
from django.shortcuts import HttpResponse 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request, 'index.html')

#@login_required
def dashboard(request):
	if request.user.baseuser.type_of_user == "patient":
		return render(request, "admin/lp-patient.html", {'user': request.user, 'agenda': True})
	else:
		return render(request, "index.html")

def dispositives(request):
	return render(request, "admin/dispositivos.html", {'user': request.user, 'dispositivos': True})

def doctors(request):
	return render(request, "admin/doctores.html", {'user': request.user, 'doctores': True})

def family(request):
	return render(request, "admin/familiares.html", {'user': request.user, 'familiares': True})

def medicine(request):
	return render(request, "admin/medicamentos.html", {'user': request.user, 'medicinas': True})

def account(request):
	return render(request, "admin/profile.html", {'user': request.user, 'cuenta': True})