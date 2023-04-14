




from django.urls import path
from . import views
from register import views as v 

# URLConf
urlpatterns = [
    path("", views.HomePageSite, name="HomePageSite"),
    path("HomePage/", views.HomePageSite, name="HomePageSite"),
    # path('',views.Main, name = "MainSite"),
    path("register/",v.register, name = "RegisterSite"),
    path("login/",v.LoginSite, name = "LoginSite"),
    path('magcalendar/', views.CalendarSite, name = "CalendarSite"),
    path("logout/",v.LogoutSite, name = "LogoutSite"),

]