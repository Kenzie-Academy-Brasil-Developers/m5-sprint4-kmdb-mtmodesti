from django.urls import path
from accounts import views

urlpatterns = [path('users/register/', views.UserView.as_view()),
               path('users/login/', views.LoginView.as_view()), path('users/', views.ListAllUsers.as_view()), path('users/<int:user_id>/', views.GetUser.as_view())]
