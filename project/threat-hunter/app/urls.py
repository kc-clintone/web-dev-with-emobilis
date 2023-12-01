from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name ='home'),
    path('result_page/<str:vulnerabilities>/', views.result_page, name='result_page'),
    path("signup/", views.signup, name = 'signup'),
    path("signin/", views.signin, name = 'signin'),
]
