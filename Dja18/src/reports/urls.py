from django.contrib import  admin
from django.conf.urls import url 

from .views import *

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='reports'),
	url(r'^api/data/$', get_data, name='api-data'),
	url(r'^api/chart/data/$',ChartData.as_view()),
	url(r'^admin', admin.site.urls),



]