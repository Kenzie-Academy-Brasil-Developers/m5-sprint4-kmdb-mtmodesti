from pickle import FALSE
from django.db import models


class ReviewChoices(models.TextChoices):
    MUST_WATCH = ("MW", "Must Watch")
    SHOULD_WATCH = ("SW", "Should Watch")
    AVOID_WATCH = ("AW", "Avoid Watch")
    NO_OPINION = ("NO", "No Opinion")


class Review(models.Model):
    
    stars = models.IntegerField()
    
    review = models.TextField()
    
    spoilers = models.BooleanField(default=False)

    recomendation = models.TextField(
        max_length=50, choices=ReviewChoices.choices, default=ReviewChoices.NO_OPINION
    )
    
    
    
    
    

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user"
    )

    movie = models.ManyToOneRel(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie",
        field_name="movie",
        to="movie",
    )
