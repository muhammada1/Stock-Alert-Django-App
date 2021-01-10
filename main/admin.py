from django.contrib import admin

# Register your models here.
from .models import WatchList, Stock

admin.site.register(WatchList)
admin.site.register(Stock)