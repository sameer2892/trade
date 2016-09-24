from django.conf.urls import url
from django.urls import reverse
from . import views

app_name = "loginapp"
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^signup', views.signup, name = "signup"),
    url(r'^signin', views.signin, name = "signin"),
    url(r'^home', views.index, name = "home"),
    url(r'^navbar', views.navbar, name = "navbar"),
    url(r'^$', views.register, name = "register")
]