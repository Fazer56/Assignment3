from django.contrib import admin

# Register your models here.
from.models import Member
from.models import Location

admin.site.register(Member)
admin.site.register(Location)
