from app1.models import Comp_Customers, Comp_data
from django.contrib import admin
from .views import *
# Register your models here.

admin.site.register(Comp_data)
admin.site.register(Comp_Customers)