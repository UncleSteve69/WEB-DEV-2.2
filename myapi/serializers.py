from rest_framework import serializers
from .models import *


class CafeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cafe
        fields = ('name', 'address', 'email', 'phone_number')


class CafeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CafeIngredient
        fields = ('cafe', 'ingredient', 'quantity')


class CocktailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cocktail
        fields = ('name', 'price', 'volume', 'alcohol', 'custom', 'time', 'cafe')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity_mu', 'price_per_unit')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('price', 'date')


class CocktailIngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CocktailIngredient
        fields = ('cocktail', 'ingredient', 'quantity')


"""
class AdditionalUserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdditionalUserInfo
"""
