from django.urls import path, include

from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetails.as_view()),
    path('groups/', views.GroupList.as_view()),
]
