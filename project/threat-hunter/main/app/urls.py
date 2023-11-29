from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name=''),
    path('', views.signup, name='signup'),
    path('', views.signin, name='signin'),
    path('', views.dashboard, name='dashboard'),
]
