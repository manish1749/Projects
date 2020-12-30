# Manish Potdar created this file

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Home</h1> " 
                        "<a href = 'http://127.0.0.1:8000/removepunc'><button type = 'button'>RemovePunc</button></a>"
                        "<a href = 'http://127.0.0.1:8000/capfirst'><button type = 'button'>CapFirst</button></a>"
                        "<a href = 'http://127.0.0.1:8000/newlineremove'><button type = 'button'>NewlineRemove</button></a>"
                        "<a href = 'http://127.0.0.1:8000/spaceremove'><button type = 'button'>SpaceRemove</button></a>"
                        "<a href = 'http://127.0.0.1:8000/charcount'><button type = 'button'>CharCount</button></a>")


def removePunc(request):
    return HttpResponse("<h1>Remove Punctuations</h1> " 
                        "<a href = 'http://127.0.0.1:8000/'><button type = 'button'>Home</button></a>")

def capFirst(request):
    return HttpResponse("<h1>Capitalize First Letter</h1> " 
                        "<a href = 'http://127.0.0.1:8000/'><button type = 'button'>Home</button></a>")

def newlineRemove(request):
    return HttpResponse("<h1>Remove New Line</h1> " 
                        "<a href = 'http://127.0.0.1:8000/'><button type = 'button'>Home</button></a>")

def spaceRemove(request):
    return HttpResponse("<h1>Remove Space</h1> " 
                        "<a href = 'http://127.0.0.1:8000/'><button type = 'button'>Home</button></a>")

def charCount(request):
    return HttpResponse("<h1>Count Characters</h1> " 
                        "<a href = 'http://127.0.0.1:8000/'><button type = 'button'>Home</button></a>")
