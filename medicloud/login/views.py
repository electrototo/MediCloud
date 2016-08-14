from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginToPage(request):
	if request.POST:
		email = request.POST['email']
		password = request.POST['pwd']

		userEmail = User.objects.get(email=email)

		print userEmail.username

		user = 	authenticate(username=userEmail.username, password=password)

		if user is not None:
			login(request, user)
			return redirect(reverse('interface:dash'))

		else:
			return redirect(reverse('interface:index'))
	else:
		return redirect(reverse('interface:index'))

def logoutUser(request):
	logout(request)

	return redirect(reverse('interface:index'))