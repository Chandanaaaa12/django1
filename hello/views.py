from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world")
def index(request):
    return render(request, "hello/index.html")
def brian(request):
    return HttpResponse("hello, Chandu")
def chandu(request):
    return HttpResponse("hello, Brain")
def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })