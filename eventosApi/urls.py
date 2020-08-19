from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('create-user/', views.Users.as_view()),
    path('api-auth/', views.Authentication.as_view()),
    path('events/', views.Events.as_view()),
    path('events/<str:eventId>', views.EventsDetail.as_view()),


]