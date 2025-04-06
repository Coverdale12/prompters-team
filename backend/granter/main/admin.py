from django.contrib import admin

from .models import *

admin.site.register(Organization)
admin.site.register(Startup)
admin.site.register(OrganizationHasUser)
admin.site.register(Investor)
