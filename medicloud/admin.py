from django.contrib.auth import Permission
from django.contrib import admin

class PermissionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Permission, PermissionAdmin)