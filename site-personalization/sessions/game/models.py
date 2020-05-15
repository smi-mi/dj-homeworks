from django.db import models


class Player(models.Model):
    games = models.ManyToManyField('Game', related_name='players', through='PlayerGameInfo')


class Game(models.Model):
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    attempts_num = models.PositiveIntegerField(default=0)
    win = models.BooleanField(default=False)
