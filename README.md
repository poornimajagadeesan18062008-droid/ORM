# Ex02 Django ORM Web Application
## Date:13-09-2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
model.py
from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
	car_name=models.CharField(max_length=10)
	fuel_type=models.CharField(max_length=10)
	manufacture_date=models.DateField()
	reg_no=models.IntegerField(Primary_key=True)
	insurance_expiry=models.DateField()
class Car_DBAdmin(admin.ModelAdmin):
	list_display=["car_name","fuel_type","manufacture_date","reg_no","insurance_expiry"]

admin.py
from Django.contrib import admin
from.models import Car_DB, Car_DBAdmin)
admin.site.register(Car_DB, Car_DBAdmin)

```


## OUTPUT

![](<Screenshot (14).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
