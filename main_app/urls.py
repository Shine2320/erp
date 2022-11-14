from django.urls import path
from .views import login,dashboard
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",dashboard),
    path('accounts/login/',
         login, name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),

]
