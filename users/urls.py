from django.urls import path


from .views import RegisterView, LoginView

urlpatterns = [
    path("users/register/", RegisterView.as_view()),
    path("users/login/", LoginView.as_view()),
]
