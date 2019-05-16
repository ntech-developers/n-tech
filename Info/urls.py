from django.conf.urls import url

from django.urls import path
from . import views


app_name = 'Info'

urlpatterns = [
    path('', views.home, name='home'),
    # url(r'home', views.home, name="home"),
]
