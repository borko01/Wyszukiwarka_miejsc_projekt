from django.db import models


# Create your models here.
class District(models.Model):
    name = models.TextField


CATEGORY = (
    (1, 'Kino'),
    (2, 'Teatr'),
    (3, 'Restauracja'),
    (4, 'Pub'),
    (5, 'Sport')
)

COOKING = (
    (1, 'Włoska'),
    (2, 'Kebab'),
    (3, 'Sushi'),
    (4, 'Chińska'),
    (5, 'Burger')
)


class Type(models.Model):
    cat = models.IntegerField(choices=CATEGORY)


class Food(models.Model):
    cuisine = models.IntegerField(choices=COOKING)


KIND = (
    (1, 'Basen'),
    (2, 'Siłownia'),
    (3, 'Studio fitness'),
    (4, 'Kort')
)


class Sport(models.Model):
    kind = models.IntegerField(choices=KIND)


class Place(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE),
    district = models.ForeignKey(District, on_delete=models.CASCADE),
    name = models.CharField(max_length=128),
    address = models.TextField,
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)


