from django.urls import path
from . import views

app_name = 'swipeSave'

urlpatterns = [
    path('', views.swipe_interface, name='swipe_interface'),
    path('bookmark-list/', views.bookmark_list, name='bookmark_list'),
    path('swipeInterface/', views.swipe_interface, name='swipeInterface'),

]
