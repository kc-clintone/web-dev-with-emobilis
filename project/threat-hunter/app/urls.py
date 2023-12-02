from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name ='home'),
    path("about/", views.about, name ='about'),
    path("analyse_with_ai/", views.analyse_with_ai, name = 'analyse_with_ai'),
    path('result_page/<str:vulnerabilities>/', views.result_page, name='result_page'),
    path("signup/", views.signup, name = 'signup'),
    path("signin/", views.signin, name = 'signin'),
    path("signout/", views.signout, name = 'signout'),
]
