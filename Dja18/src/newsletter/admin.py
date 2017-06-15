from django.contrib import admin
from .forms import *

from .models import *
# Register your models here.

class signUpAdmin(admin.ModelAdmin):
	list_display=["full_name","email"]
	form=SignUpForm
	
	# class Meta: 
	# 	model=SignUp 

class LoginAdmin(admin.ModelAdmin):
	list_display=["email","password"]
	form= LoginForm


admin.site.register(Post) 
admin.site.register(SignUp, signUpAdmin)
admin.site.register(Login, LoginAdmin)
