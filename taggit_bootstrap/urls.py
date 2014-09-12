from django.conf.urls import patterns, url
from .views import *
urlpatterns = patterns('', 
		url(r'^$',TaggitBoostrapView.as_view(),name='taggit-bootstrap')
	)
