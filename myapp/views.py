from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models import Employee
from myapp.permissions import IsSuperUser
from myapp.serializers import UserSerializer


# Create your views here.
class Register(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsSuperUser]
    def post(self, request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
class employeelist(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsSuperUser]
    def get(self, request):
        s=Employee.objects.all()
        serializer_instance=UserSerializer(s,many=True)
        return Response(serializer_instance.data)
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
class employee_detail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsSuperUser]
    def get(self, request,i):
        get_object_or_404(Employee,id=i)
        serializer_instance=UserSerializer(data=request.data)
        return Response(serializer_instance.data)
    def put(self, request, i):
        get_object_or_404(Employee,id=i)
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, i):
        s=Employee.objects.get(id=i)
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
