from django.urls import path
from . views import HelloWorld

app_name = 'myapp'


urlpatterns = [
    path('', HelloWorld, name='helloworld'),
]
