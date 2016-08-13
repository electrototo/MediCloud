from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login


from django.shortcuts import redirect

# Create your views here.
def loginUser(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)

	else:
		return redirect('interface:index', kwargs={'c': 'Invalid Username or Password'})

#def createUser(request):


def index(request):
	return HttpResponse('Hola')