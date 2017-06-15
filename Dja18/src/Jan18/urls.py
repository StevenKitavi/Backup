from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('newsletter.urls')),

    # url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^register/$', 'newsletter.views.register', name='register' ),
    # url(r'^list/$', 'newsletter.views.post_list',name='list'),
    # url(r'^create/$', 'newsletter.views.post_create', name='create'),
    # url(r'^(?P<id>\d+)/$', 'newsletter.views.post_detail', name='detail'),
    # url(r'^(?P<id>\d+)/edit/$','newsletter.views.post_update', name='update'),
    # url(r'^(?P<id>\d+)/delete/$', 'newsletter.views.post_delete', name='delete'),
    # url(r'^login/$', 'newsletter.views.login', name='login'),
    # url(r'^User_dashboard/$', 'newsletter.views.admin_dashboard', name='User_dashboard'),



    url(r'^about/$', 'Jan18.views.about', name='about'),
    url(r'^contact/$', 'Jan18.views.contact', name='contact'), 
    url(r'^home_business/$', 'Jan18.views.home_business', name='home_business'), 

    
    

    # url(r'^accounts/', include(accounts.registration.urls)),
  

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

