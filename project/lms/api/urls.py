# urls.py
from django.urls import path
from .views import CourseList

urlpatterns = [
    path('api/courses/', CourseList.as_view(), name='course-list'),
    # Add other URL patterns as needed
]

