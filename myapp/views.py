from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .serializers import StudentSerializer

# Create your views here.

@api_view(('GET',))
def HelloWorld(request, format=None):
    '''
    FUNCTION BASED APIS IS VERY BAD FOR EVERYTHING,
    WE NEED TO DECORATOR CHAINING EXAMPLE GET AND POST
    '''

    return Response({'id':'1','Name': 'Mithilesh yadav from function based hello World!'})
    
