from django import forms
from django.core import validators


from .models import *

class SignUpForm(forms.ModelForm):
	full_name = forms.CharField(required=True)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password_again = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = SignUp
		fields='full_name', 'email','password','password_again'




class LoginForm(forms.ModelForm):
	email=forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Login
		fields='email','password'


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields= 'title', 'category' ,'description', 'location' , 'image',
			    
			    
			    
			    


		





	def clean_email(self):
		email =self.cleaned_data.get('email')
		email_base, provider= email.split("@")
		domain, extension= provider.split('.')

		return email



	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name


	def clean_password(self):
		password=self.cleaned_data.get('password')
		return password


	def clean_password(self):
		password_again=self.cleaned_data.get("password_again")
		return password_again

 	