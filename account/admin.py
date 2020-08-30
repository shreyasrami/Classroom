from django.contrib import admin
from account.models import Teacher,Student
# Register your models here.


admin.site.register((Teacher,Student))