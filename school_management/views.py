from django.shortcuts import render
from user_management.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *


class SchoolView(APIView):
    @staticmethod
    def post(request):
        serializer = SchoolPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = School.objects.all()
        return Response(SchoolGetSerializer(instance=queryset, many=True).data)


class EventView(APIView):
    @staticmethod
    def post(request):
        serializer = EventPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Event.objects.all()
        return Response(EventGetSerializer(instance=queryset, many=True).data)


class UserSchoolView(APIView):
    @staticmethod
    def post(request):
        serializer = UserSchoolPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = UserSchool.objects.all()
        return Response(UserSchoolGetSerializer(instance=queryset, many=True).data)


class ApplicationView(APIView):
    @staticmethod
    def post(request):
        serializer = ApplicationPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Application.objects.all()
        return Response(ApplicationGetSerializer(instance=queryset, many=True).data)


class DocumentView(APIView):
    @staticmethod
    def post(request):
        serializer = DocumentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        return Response(serializer.errors)

    @staticmethod
    def get(request):
        queryset = Document.objects.all()
        return Response(DocumentnGetSerializer(instance=queryset, many=True).data)


