from django.shortcuts import render, redirect
from account.models import Account
from myapi.models import Cocktail
from django.contrib.auth.forms import UserChangeForm


def blog(request):
    # you have to create additional user info
    user = Account.objects.all()[0]
    args = {'user': user}
    return render(request, 'blog.html', args)
