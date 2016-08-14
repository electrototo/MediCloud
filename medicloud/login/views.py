from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.shortcuts import redirect

# Create your views here.
def loginUser(request):
	email = request.POST['email']
	password = request.POST['pwd']

	username = User.objects.get(email=email).username

	print username
	print password

	user = authenticate(username=username, password=password)

	print user

	if user is not None:
		login(request, user)

		return redirect('interface:user')

	else:
		return redirect('interface:index')

def logout(request):
	logout(request)

	return redirect('interface:index')


def index(request):
	return HttpResponse('Hola')