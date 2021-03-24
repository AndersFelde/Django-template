from django.shortcuts import render
#  from webpage.models import TestModal


def test1(request):
    return render(request, "webpage/test1.html")
