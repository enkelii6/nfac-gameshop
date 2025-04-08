from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORIES = [
        ('psn_key', 'PSN Key'),
        ('steam_key', 'Steam Key'),
        ('xbox_key', 'Xbox Key'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
