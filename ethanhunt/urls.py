from . import views
from django.urls import path

urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/",views.signup,name="signup"),
]