




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


    #AJAX
    path('get_data',views.get_data, name='get_data'),
    path('show_day_calendar',views.show_day_calendar, name='show_day_calendar'),
    path('delete_row',views.delete_row,name='delete_row')

]