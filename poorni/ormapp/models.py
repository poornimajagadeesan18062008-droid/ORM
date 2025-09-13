from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
	car_name=models.CharField(max_length=10)
	fuel_type=models.CharField(max_length=10)
	manufacture_date=models.DateField()
	reg_no=models.IntegerField(primary_key=True)
	insurance_expiry=models.DateField()
class Car_DBAdmin(admin.ModelAdmin):
	list_display=["car_name","fuel_type","manufacture_date","reg_no","insurance_expiry"]

