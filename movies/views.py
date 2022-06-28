from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import MovieSerializer
from movies.models import Movie
from rest_framework import status
from movies.permissions import MoviePermission, ReviewPermission
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class MovieView(APIView):

    permission_classes = [MoviePermission]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        movies = Movie.objects.all()
        serializer_response = MovieSerializer(movies, many=True)
        return Response(serializer_response.data)


class ListMovieByIdReview(APIView):

    permission_classes = [MoviePermission]

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer_response = MovieSerializer(movie)
            return Response(serializer_response.data)
        except Movie.DoesNotExist:
            return Response({'message': 'not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(
                movie, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({'message': 'not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response({'message': 'movie deleted.'})
        except Movie.DoesNotExist:
            return Response({'message': 'not found.'}, status=status.HTTP_404_NOT_FOUND)


class MovieReviewsView(APIView):

    permission_classes = [ReviewPermission]

    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = ReviewSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save(movie_id=movie, critic=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Movie.DoesNotExist:
            return Response({'message': 'movie not found.'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            reviews = Review.objects.filter(movie_id=movie)

            serializer = ReviewSerializer(reviews, many=True)

            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({'message': 'movie not found.'}, status=status.HTTP_404_NOT_FOUND)


class DeleteReview(APIView):

    permission_classes = [ReviewPermission]

    def delete(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
            if request.user.is_superuser or review.critic.id == request.user.id:
                review.delete()
                return Response({'message': 'review deleted successfully.'})
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        except Review.DoesNotExist:
            return Response({'message': 'review not found.'}, status=status.HTTP_404_NOT_FOUND)


class AllReviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer_response = ReviewSerializer(reviews, many=True)
        return Response(serializer_response.data)
