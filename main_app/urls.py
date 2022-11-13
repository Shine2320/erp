from django.urls import path
from .views import login,dashboard

urlpatterns = [
    path("",dashboard),
    path('login/',login)

]
