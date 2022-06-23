from movies.models import Movie

class Helper:
    def get_or_crete_genre(genre_group):
        genre = []
        try:
            genre = Movie.objects.get(genre=genre_group["name"])
            print('oi')
        except:
            genre = Movie.objects.create(**genre_group)
            print('tchau')
        print(genre)
        return genre
    