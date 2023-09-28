from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getData(request):
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return Response(data)