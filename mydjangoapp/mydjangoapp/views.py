from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'base.html')
    # return HttpResponse('Text Utility')


def removepunc(request):
    return HttpResponse("<h1>Remove Punc <a href='/'>back</a>")


def capfirst(request):
    return HttpResponse('Capitalize first')


def newlineremove(request):
    return HttpResponse('Remove Newline')


def spaceremove(request):
    return HttpResponse('Remove Space')


def charcount(request):
    return HttpResponse('Count characters')


def temp_test(request):
    return render(request, 'base.html')
