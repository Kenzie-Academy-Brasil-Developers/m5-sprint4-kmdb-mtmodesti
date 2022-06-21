
from pickle import FALSE
from django.db import models

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.TextField(max_length=50)
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='user')
    
    movie = models.ManyToOneRel("movies.movie", on_delete=models.CASCADE, related_name='movie', field_name='movie', to='movie' )
    
    
    