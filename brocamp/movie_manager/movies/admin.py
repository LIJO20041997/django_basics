from django.contrib import admin
from .models import Movieinfo, Director,CensorInfo, Actor

# Register your models here.

admin.site.register(Movieinfo)
admin.site.register(Director)
admin.site.register(CensorInfo)
admin.site.register(Actor)
