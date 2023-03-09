from django.shortcuts import render

from django.http import HttpResponse


def second(request):
    return HttpResponse("<h1> This is the second function</h1>")