from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Task
from api.serializers import TaskSerializer

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

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all() #model에서 Task 데이터를 가져옴
	serializer = TaskSerializer(tasks, many=True)# 가져온 데이터를 Serializer로 serializing함
	return Response(serializer.data) #serializing된 데이터를 response로 내보냄
	