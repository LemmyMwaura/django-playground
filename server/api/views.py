from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

@api_view
def api_home(request, *args, **kwargs):
  return JsonResponse({"message": "Hi, There, This is your Django API"})

