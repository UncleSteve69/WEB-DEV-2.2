from django.shortcuts import render, redirect
from myapi.models import Cocktail


def home(request):
    # you have to create additional user info
    Cocktails = Cocktail.objects.all()
    list(Cocktails)
    args = {'Cocktail1': Cocktails[0],
            'Cocktail2': Cocktails[1],
            'Cocktail3': Cocktails[2],
            'Cocktail4': Cocktails[3],
            'Cocktail5': Cocktails[4],
            'Cocktail6': Cocktails[5],
            'Cocktail7': Cocktails[6],
            'Cocktail8': Cocktails[7]}
    return render(request, 'home.html', args)
