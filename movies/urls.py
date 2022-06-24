from django.urls import path

from .views import MoviesView, MovieIdView, MovieReviewById


urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>", MovieIdView.as_view()),
    path("movies/<int:movie_id>/reviews", MovieReviewById.as_view()),
    
]
