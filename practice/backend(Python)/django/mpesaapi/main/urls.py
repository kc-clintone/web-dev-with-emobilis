from django.urls import path

from main import views


app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('token', views.token, name='token'),
    path('pay', views.pay, name='pay'),
    path('stk', views.stk, name="stk")

]
