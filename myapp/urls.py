from django.urls import path
from . views import HelloWorld, StudentAPI_Create_Get

app_name = 'myapp'


urlpatterns = [
    path('helloworld/', HelloWorld, name='helloworld'),
    path('student_create_get/', StudentAPI_Create_Get.as_view(), name='student_create_get'),
]
