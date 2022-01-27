from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def apiOverview(request):
    '''url 패턴을 모두 보여주는 view임, Json 패턴을 dictionary형태의 데이털 뿐임'''
    return JsonResponse("API BASE POINT", safe=False)