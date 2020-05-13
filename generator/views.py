from django.shortcuts import render # use the " templates " folder
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    # First try: HttpResponse('Ghaith Ben Amor')

    #use the " templates "" folder
    return render(request, 'generator/home.html')


def password(request): # request contien the informations inside url ex: uppercase=on
    # return HttpResponse('<h1>Jawher Ben Amor</h1>')


    Characters=list('azetyuiopmlkjhgfdsqwxcvbn')

    if request.GET.get('uppercase'):
        Characters.extend(list('AZERTYUIOPMLKJHGFDSQWXCVBN'))

    if request.GET.get('special'):
        Characters.extend(list('$*!&()'))

    if request.GET.get('numbers'):
        Characters.extend(list('123456789'))

    length =  int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(Characters)
    return render(request, 'generator/password.html', {'password':thepassword})
