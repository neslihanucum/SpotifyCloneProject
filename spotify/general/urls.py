from django.urls import path
from general.views import home

app_name = 'general'

urlpatterns = [
    path('', home, name="home"),
]

