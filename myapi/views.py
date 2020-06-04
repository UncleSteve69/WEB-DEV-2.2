from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all().order_by('name')
    serializer_class = CafeSerializer


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all().order_by('name')
    serializer_class = CocktailSerializer


"""@login_required
@user_passes_test(lambda u: u.groups.filter(name='Unauthorized').count() == 0, login_url='/myapp/denied/')
@user_passes_test(lambda u: u.groups.filter(name='Authorized').count() == 0, login_url='/myapp/denied/')"""


class CafeIngredientViewSet(viewsets.ModelViewSet):
    queryset = CafeIngredient.objects.all().order_by('name')
    serializer_class = CafeIngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('name')
    serializer_class = OrderSerializer


class CocktailIngredientViewSet(viewsets.ModelViewSet):
    queryset = CocktailIngredient.objects.all().order_by('name')
    serializer_class = CocktailIngredientSerializer


"""
class AdditionalUserInfoViewSet(viewsets.ModelViewSet):
    queryset = AdditionalUserInfo.objects.all().order_by('user')
    serializer_class = AdditionalUserInfoSerializer
"""
