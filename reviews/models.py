from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ChoicesRecomendation(models.TextChoices):
    MUST_WATCH = ("Must Watch", "MW")
    SHOULD_WATCH = ("Should Watch", "SW")
    AVOID_WATCH = ("Avoid Watch", "AW")
    NO_OPINION = ("No Opinion", "NO")


class Review(models.Model):
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    
    recomendation = models.CharField(
        max_length=50, choices=ChoicesRecomendation.choices, default=ChoicesRecomendation.NO_OPINION)
    movie_id = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews")
    
    critic = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="reviews")
