from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user-profile/<str:pk>/', views.user_profile, name="user-profile"),
    path('register/', views.registerUser, name="register"),
    path('add-project/', views.addProject, name="add-project"),
    path('add-skill/', views.addSkill, name="add-skill"),
    path('developers/', views.getDevelopers, name="developers"),
    path('inbox/<str:pk>/', views.inbox, name="inbox"),
    path('message-inbox/<str:pk>/', views.messageInbox, name="messageInbox"),
    path('send-message/<str:pk>/', views.sendMessage, name="sendMessage"),
]