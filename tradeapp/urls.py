from django.conf.urls import url
from . import views

app_name = "tradeapp"
urlpatterns = [
    # url(r'^signup/$', views.signup, name="signup"),
    # url(r'^signin/$', views.signin, name="signin"),
    # url(r'^$', views.home, name="home"),
    # url(r'^home/$', views.home, name = "home1"),
    # url(r'^logout/$', views.user_logout, name="user_logout"),
    # url(r'^edit_profile/$', views.edit_profile, name="settings"),
    url(r'^read_json/$', views.read_json, name="read_json")
]