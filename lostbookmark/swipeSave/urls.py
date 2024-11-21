from django.urls import path
from . import views

urlpatterns = [
    path('', views.swipe_interface, name='swipe_interface'),
]
