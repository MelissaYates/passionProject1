from rest_framework import viewsets
from .models import CourseUser, Subject, Course, RelatedCourse, Module, Content, ItemBase, Text, File, Image, Video
from .serializers import UserSerializer, SubjectSerializer, CourseSerializer, RelatedCourseSerializer, ModuleSerializer, ContentSerializer, ItemBaseSerializer, TextSerializer, FileSerializer, ImageSerializer, VideoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CourseUser.objects.all()
    serializer_class = UserSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
#
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RelatedCourseViewSet(viewsets.ModelViewSet):
    queryset = RelatedCourse.objects.all()
    serializer_class = RelatedCourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
#
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ItemBaseViewSet(viewsets.ModelViewSet):
    queryset = ItemBase.objects.all()
    serializer_class = ItemBaseSerializer

class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
#
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
#
