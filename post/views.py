from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()

    time = data["time"]["updated"]
    usd = data["bpi"]["USD"]["rate"]
    gbp = data["bpi"]["GBP"]["rate"]
    eur = data["bpi"]["EUR"]["rate"]
    context = {'usd':usd, 'gbp':gbp, 'eur':eur, 'time':time}

    if request.htmx:
        return render(request, 'post/partials/bitcoin.html', context)
    else:
        return render(request, 'post/index.html', context)