
from django.shortcuts import render
from django.conf import settings

def home_business(request):
	title='View Business'

	context = {
	"title":title,
	}


 	return render(request, "home_business.html",context)


def contact(request):
 	title='contact'

 	context={
 	"title": title,
 	}


 	return render(request, "contact.html", context)



def about(request):
 	title ='About Us'

 	context={
 	"title": title,
 	}

 	return render(request, "about.html", context) 