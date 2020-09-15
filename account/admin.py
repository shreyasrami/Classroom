from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from account.models import User,Teacher,Student
# Register your models here.

@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = ("name","username","email")
    list_filter = ("is_admin","is_teacher")
    search_fields = ("first_name","last_name")
    ordering = ("first_name",)

    filter_horizontal = ()
    
    
@admin.register(Teacher)
class TeacherAdmin(BaseAdmin):
    list_display = ("name","username","email")
    list_filter = ("department","subject",)
    search_fields = ("first_name","last_name")
    ordering = ("first_name",)
    
    filter_horizontal = ()
    

@admin.register(Student)
class StudentAdmin(BaseAdmin):
    list_display = ("sap_id","name","email")
    list_filter = ("department","division")
    search_fields = ("sap_id",)
    ordering = ("sap_id",)

    filter_horizontal = ()
    
