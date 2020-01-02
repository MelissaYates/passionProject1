from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User, Subject, Course, RelatedCourse, Module, Content, ItemBase, Text, File, Image, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = '__all__'


class RelatedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedCourse
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields = '__all__'


class ItemBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBase
        fields = "__all__"


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = "text"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields = 'file'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "file"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "url"


