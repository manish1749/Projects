# Manish Potdar created this file

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Manish Potdar</h1>")


def display(request):
    f = open("C:\\Users\\Manish\\PycharmProjects\\Projects\\mysite\\xyz.txt", "r")
    return HttpResponse(f.read())