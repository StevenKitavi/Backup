from django.db import models
from django import forms
from django.core.urlresolvers import reverse

#models 
class SignUp(models.Model):
	email= models.EmailField()
	full_name=models.CharField(max_length=120,default='',blank=True, null=True)
	password = models.CharField(max_length=120, default='', blank=True, null=True)
	password_again = models.CharField(max_length=120, default='', blank=True, null=True )


class Login(models.Model):
	email = models.EmailField(max_length=120, default='', blank=True, null=True)
	password = models.CharField(max_length=120, default='', blank=True, null=True)



	



	
	def __unicode__(self):

		return self.email


class Post(models.Model):
	title=models.CharField(max_length=120)
	image = models.ImageField(null=True, blank=True,
		    width_field="width_field", 
		    height_field="height_field")
	height_field= models.IntegerField(default=50)
	width_field= models.IntegerField(default=50)
	category= models.TextField(default='Nai Hustle')
	description = models.TextField(default='watch what you wear')
	location= models.TextField(max_length=120 ,default="Moi avenue Imax Building floor 4 stall 23")
	updated =models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)




	def __unicode__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("detail", kwargs={"id": self.id})
		


	class Meta:
		ordering = ["-timestamp", "-updated"]
