




from django.urls import path
from . import views
from register import views as v 

# URLConf
urlpatterns = [
    path('', views.mainsite),
    path("register/",v.register, name = "RegisterSite"),
    path("login/",v.LoginSite, name = "LoginSite"),
    path('magcalendar/', views.say_hello, name = "CalendarSite"),
    path("logout/",v.LogoutSite, name = "LogoutSite")
]