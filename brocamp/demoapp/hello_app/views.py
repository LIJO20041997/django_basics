from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_hello(request):
    return HttpResponse("<h1>hello world </h1>")


# render a template
def first_page(request):
    movie_list = [{
        'title':"Godfather", 
        'year':1990,
        'summary':"Story of a underworld gangster",
        'success':True
    },
    {
        'title':"Titanic", 
        'year':2002,
        'summary':"Story of Love",
        'success':True
    },
    {
        'title':"Avengers", 
        'year':2010,
        'summary':"Story of a Super Heros",
        'success':True
    }]
    return render(request, "index.html", {"movie_list":movie_list})