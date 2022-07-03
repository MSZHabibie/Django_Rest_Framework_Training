from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from djrfapp.serializers import StudentSerializer
from djrfapp.models import Student

class TesView(APIView):
   def get(self, request, *args, **kwargs):
      queryset = Student.objects.all()
      serializer = StudentSerializer(queryset, many=True)
      return Response(serializer.data)

   def post(self, request, *args, **kwargs):
      serializer = StudentSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)