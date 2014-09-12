from django.shortcuts import render
from django.views.generic import View
from django import http
from taggit.models import Tag

class TaggitBoostrapView(View):
	def get(self, request, *args, **kwargs):
		query=request.GET.get('query')
		tag_list=Tag.objects.filter(name__startswith=query).all()
		result=[{'Id':tag.name,'value':tag.name} for tag in tag_list]
		return http.JsonResponse(result,safe=False)

