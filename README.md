<img src='./Screenshot from 2022-06-28 09-06-05.png' alt='DER'>DER</img>

In this project i created a DER, as you can see in the picture, with Python and Django Rest Framework. Token authentication, exclusive features of administrative users and a sql3 database was used to build this.


movie = get_object_or_404(Movie, pk=movie_id)
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(critic=request.user, movie_id=movie)
        return Response(serializer.data, status.HTTP_201_CREATED)
