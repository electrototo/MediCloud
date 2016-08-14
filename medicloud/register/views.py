from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def sendmail(request):
	return JsonResponse({'error':1})

def getAlarm(request):
	return 	JsonResponse({'name': 'Humberto', 'type_of_alert': 1, 'description': 'El familiar humberto no ha tomado su medicamento: Ibuprofeno'})