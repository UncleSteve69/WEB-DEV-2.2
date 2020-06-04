from django.db import models
from django.contrib.auth.decorators import login_required, user_passes_test
from account.models import Account


class Cafe(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone_number = models.IntegerField()

    def __str__(self):
        return "%s" % self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField(max_length=60)
    volume = models.FloatField()
    alcohol = models.BooleanField()
    custom = models.BooleanField()
    time = models.FloatField()
    cafe = models.ManyToManyField(Cafe)
    img = models.CharField(max_length=60)

    def __str__(self):
        return "%s" % self.name


class Order(models.Model):
    price = models.FloatField(max_length=60)
    date = models.DateField(max_length=60)
    amount_of_cocktails = models.ManyToManyField(Cocktail)
    # user = models.ManyToManyField(User)

    def __str__(self):
        return "%s %s %s" % (self.price, self.date, self.amount_of_cocktails)


class Ingredient(models.Model):
    name = models.CharField(max_length=60)
    quantity_mu = models.CharField(max_length=20)
    price_per_unit = models.FloatField(max_length=60)

    def __str__(self):
        return "%s" % self.name


class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return "%s %s" % (self.cocktail.name, self.ingredient.name)


class CafeIngredient(models.Model):
    cafe = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.cafe, self.ingredient)

"""
class User(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    age = models.IntegerField('User age', blank=True)
    gender = models.CharField('User gender',
                              blank=True, max_length=20)
    user_menu = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

"""

"""
class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.user, self.dark_mode)
"""