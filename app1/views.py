from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def xyz(request):
    return render(request, "index.html")


def signUp(request):
    print("signUp method is working");
    return render(request, "index.html")
