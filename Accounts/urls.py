from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


app_name = 'Accounts'

urlpatterns = [
    path('login/',   auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('register/',  views.registration_form, name="register"),
    path('profile/',  views.profile, name="profile"),
]

