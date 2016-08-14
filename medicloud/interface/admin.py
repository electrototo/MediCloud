from django.contrib import admin
from .models import baseUser, doctorExtent, Meds, patientExtent

# Register your models here.
admin.site.register(baseUser)
admin.site.register(doctorExtent)
admin.site.register(Meds)
admin.site.register(patientExtent)