from django.contrib import admin

# Register your models here.
from area.models import Area
from provider.models import Provider

admin.site.register(Provider)

