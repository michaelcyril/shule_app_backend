from rest_framework import serializers
from .models import *



class SchoolPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'user',
            'name',
            'email',
            'location',
            'type'
        ]


class SchoolGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'id',
            'user',
            'name',
            'email',
            'location',
            'type'
        ]
        depth = 2


class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'school',
            'title',
            'description',
            'event_at',
            'created_at'
        ]


class EventGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'school',
            'title',
            'description',
            'event_at',
            'created_at'
        ]
        depth = 2




class UserSchoolPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSchool
        fields = [
            'user',
            'school'
        ]


class UserSchoolGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSchool
        fields = [
            'id',
            'user',
            'school'
        ]
        depth = 2



class ApplicationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'user',
            'school',
            'student_name',
            'age',
            'created_at'
        ]


class ApplicationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            'user',
            'school',
            'student_name',
            'age',
            'created_at'
        ]
        depth = 2




class DocumentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'application',
            'document'
        ]


class DocumentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id',
            'application',
            'document'
        ]
        depth = 2

