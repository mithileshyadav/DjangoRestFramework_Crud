from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .serializers import StudentSerializer
from .models import Student

# Create your views here.

@api_view(('GET',))
def HelloWorld(request, format=None):
    '''
    FUNCTION BASED APIS IS VERY BAD FOR EVERYTHING,
    WE NEED TO DECORATOR CHAINING EXAMPLE GET AND POST
    '''

    return Response({'id':'1','Name': 'Mithilesh yadav from function based hello World!'})
    

'''THIS CLASS BASED API FOR CREATE NEW RECORD AND GET ALL DATA '''
class StudentAPI_Create_Get(APIView):
    serializer_class = StudentSerializer

    # USE FOR GET THE DATA WITHE THE HELP OF API
    def get(self, request, format = None):
        data = Student.objects.filter()
        if len(data):
            serialize = self.serializer_class(data, many=True)
            serialize_data = serialize.data
            return Response(serialize_data, status=status.HTTP_200_OK)
        else:
            return Response({'No Data Found!'}, status=status.HTTP_200_OK)


    # POST DATA FOR SAVE DATA
    def post(self, request, format = None):
        # code for create new data
        print(request.data, '+++++++++++++++++ post data \n')
        serialize = self.serializer_class(data=request.data)
        if serialize.is_valid():
            serialize.save()
            current_data = serialize.data
            return Response(current_data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

            
