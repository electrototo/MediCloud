from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class baseUser(models.Model):
	type_of_user = models.CharField(max_length=20, blank=False)
	attached = models.OneToOneField(User)

	def __str__(self):
		return self.attached.username

class doctorExtent(models.Model):
	basicInformation = models.CharField(max_length=400)

	doctor = models.OneToOneField(User)	

	def __str__(self):
		return self.doctor.username

class Meds(models.Model):
	name = models.CharField(max_length=30, blank=False)

	beginDate = models.DateField()
	endDate = models.DateField()

	instructions = models.CharField(max_length=500, blank=True)
	lapse = models.IntegerField(blank=False)

	def __str__(self):
		return self.name

class patientExtent(models.Model):
	meds = models.ManyToManyField(Meds, blank=True)
	doctor = models.ManyToManyField(doctorExtent, blank=True)

	patient = models.OneToOneField(User, blank=True)

	dob = models.DateField()
	gender = models.CharField(max_length=30, blank=True)
	ocupation = models.CharField(max_length=500, blank=True)
	height = models.FloatField(blank=True)
	weight = models.FloatField(blank=True)

	blood = models.CharField(max_length=500, blank=True)
	alergies = models.CharField(max_length=500, blank=True)

	diagnostic = models.CharField(max_length=500, blank=True)

	responsible = models.EmailField(blank=True)

	def __str__(self):
		return self.patient.username