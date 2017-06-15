from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404, redirect, Http404

from .forms import *
from .models import *


#views




def home(request):
	title='Welcome'
	form = SignUpForm(request.POST or None)

	context= {
		"title": title,
    	"form": form,
    }

	

	if form.is_valid():
		instance= form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "new full name"

		instance.full_name = full_name
		instance.save()
		context = { 
		"title": "Thank You"
		}
		

	

	return render(request, "home.html",context)
	#return render(request, "example.html, context")





def register(request):
	title ='Register'
	form =SignUpForm(request.POST or None)
	if form.is_valid():
		
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
 		form_full_name = form.cleaned_data.get("full_name")
		subject = 'Site contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youtotheotheremail@gmail.com']
		contact_message="%s: %s via %s"%(
				form_full_name,
				form_message,
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject,
			    contact_message,
			    from_email,
			    [to_email], 
			    html_message = some_html_message,
			    fail_silently= True)

	context={
	"form":form,
	"title": title,

	}


	return render(request, "register.html", context)



def login(request):
	title="Login"
	form= LoginForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_password = form.cleaned_data.get("password")

	context={
	"title": title,
	"form": form,

	}
	return render(request, "login.html", context)



def post_create(request):
	title="Create"
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		messages.success(request, "Succesfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		messages.error(request, "Not Succesfully Created")
	
	context ={
	    "title": title,
	    "form": form,
	}
	

	return render(request,"post_form.html", context)
 

def post_detail(request, id=None):
	instance= get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None)
	context ={
		"title": instance.title,
		"instance":instance,
		
	}
	return render(request, "post_detail.html", context)


def post_list(request):
	title="List"
	queryset_list = Post.objects.all().order_by("-timestamp")  
	query = request.GET.get("business")
	if query:
		queryset_list =queryset_list.filter(
				Q(title__icontains=query) |
				Q(description__icontains=query)|
				Q(category__icontains=query) |
				Q(location__icontains=query)

				) .distinct()

	paginator = Paginator(queryset_list, 5)

	page = request.GET.get('page')
	try:
		queryset =  paginator.page(page)
	except PageNotAnInteger:
		#if Page Not an interger deliver first page
		queryset= paginator.page(1)
	except EmptyPage:
		#if page is out of range deliver the last page of the results
		queryset = paginator.page(paginator.num_pages)


	context ={
	    "object_list": queryset,
		"title":title
	}
	return  render(request,"post_list.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None , request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context={
		"title": instance.title,
		"instance": instance,
		"form": form
	}
	return  render(request, "post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Deleted")
	
	return redirect("newsletter:list")


def find_business( request):
	title="find_business"
	queryset_list = Post.objects.all().order_by("-timestamp")
	query=request.GET.get("naay")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(description__icontains =query)|
			Q(category__icontains=query)|
			Q(location__icontains=query)
			) .distinct()

	paginator = Paginator(queryset_list, 5)

	page = request.GET.get('page')
	try:
		queryset =  paginator.page(page)
	except PageNotAnInteger:
		#if Page Not an interger deliver first page
		queryset= paginator.page(1)
	except EmptyPage:
		#if page is out of range deliver the last page of the results
		queryset = paginator.page(paginator.num_pages)
	context={
		"object_list":queryset,
		"title": title
	}
	return render(request, "home_business.html", context)


def User_dashboard(request):
	title="admin_dashboard"
	context={
		"title":title

	}
	return render(request, "User_dashboard.html", context)







