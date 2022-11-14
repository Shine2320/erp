from django.urls import path
from .views import login_request,dashboard,add_user,view_user,logout_request
from django.contrib.auth import views as auth_views
urlpatterns = [
     path("",dashboard),
     path('accounts/login/',
          login_request, name='login'),
     path('logout/',
         logout_request, name='logout'),
     path("view_user/",view_user,name='view_user'),
     path("view_user/add_user/",add_user,name='add_user'),

]
