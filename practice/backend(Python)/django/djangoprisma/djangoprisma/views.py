from rest_framework import generics
from django.shortcuts import render
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

def Home(request):
    return render(request, 'index.html')
