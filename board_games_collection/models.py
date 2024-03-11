from django.db import models


class BoardGames(models.Model):
    tesera_id = models.IntegerField()
    tesera_name = models.CharField(max_length=1024)
    tesera_rating_user = models.FloatField()
    tesera_n10_rating = models.FloatField()
    bgg_id = models.IntegerField()
    bgg_name = models.CharField(max_length=1024)
    bgg_average_rating = models.FloatField()
    bgg_bayes_average_rating = models.FloatField()
    bgg_rank = models.IntegerField()
    bgg_weight = models.FloatField()
