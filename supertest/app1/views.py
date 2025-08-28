from django.shortcuts import render
import requests
import math
from django.http import HttpResponse
# Create your views here.
def index(request):
    #пункт 1
    response = requests.get("https://catfact.ninja/facts")
    if response.status_code == 200:
        data = response.json()
        #пункт 2
        total = data.get("total")
        print(total)
        #пункт 3
        per_page = data.get("per_page")
        print(per_page)
        #пункт 4
        last_page = math.ceil(total / per_page)
        response_last = requests.get("https://catfact.ninja/facts", params={"page": last_page})
        data_last = response_last.json()
        facts = data_last.get("data")
        print(facts)
        #пункт 5
        shortest_fact = min(facts, key=lambda x: x["length"])
        print(shortest_fact)
    return HttpResponse("ok")