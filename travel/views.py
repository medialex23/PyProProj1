from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Bob'

#    return HttpResponse(html.format(name))
    return render(request, 'home.html', {'name': name})
