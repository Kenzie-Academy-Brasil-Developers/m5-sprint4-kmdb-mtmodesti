from django.urls import path
from movies import views

urlpatterns = [path('movies/', views.MovieView.as_view()),
               path('movies/<int:movie_id>/', views.ListMovieByIdReview.as_view()), path('movies/<int:movie_id>/reviews/', views.MovieReviewsView.as_view()), path('reviews/', views.AllReviews.as_view()), path('reviews/<int:review_id>/', views.DeleteReview.as_view())]
