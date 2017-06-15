from django.conf.urls import url 


urlpatterns = [
		url(r'^home/$', 'newsletter.views.home', name='home'),
		url(r'^register/$', 'newsletter.views.register', name='register' ),
		url(r'^list/$', 'newsletter.views.post_list',name='list'),
		url(r'^create/$', 'newsletter.views.post_create', name='create'),
		url(r'^(?P<id>\d+)/$', 'newsletter.views.post_detail', name='detail'),
		url(r'^(?P<id>\d+)/edit/$','newsletter.views.post_update', name='update'),
		url(r'^(?P<id>\d+)/delete/$', 'newsletter.views.post_delete', name='delete'),
		url(r'^login/$', 'newsletter.views.login', name='login'),
		url(r'^User_dashboard/$', 'newsletter.views.User_dashboard', name='User_dashboard'),
		url(r'^find_business/$', 'newsletter.views.find_business', name='find_business'),
]