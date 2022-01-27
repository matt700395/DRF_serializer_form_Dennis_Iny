from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

'''url 패턴을 모두 보여주는 view임, Json 패턴을 dictionary형태의 데이털 뿐임'''
@api_view(['GET'])
def apiOverview(request):

	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)