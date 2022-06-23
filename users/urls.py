from django.urls import path


from .views import RegisterView, LoginView, UserView, UserViewById

urlpatterns = [
    path("users/register/", RegisterView.as_view()),
    path("users/login/", LoginView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<int:user_id>", UserViewById.as_view()),
]
