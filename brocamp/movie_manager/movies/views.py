from django.shortcuts import render, HttpResponse
from . models import Movieinfo
from . forms import MovieForm

# Create your views here.

def create(request):
    
    if request.POST:
        frm=MovieForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return HttpResponse("Movie added successfully")

    else:
        frm = MovieForm()
    return render(request, 'create.html',{'frm':frm})
    

def list(request):
    movie_data = Movieinfo.objects.all()
    return render(request, 'list.html', {'movies':movie_data})

def edit(request,pk):
    instance = Movieinfo.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST, instance=instance)
        if frm.is_valid():
            frm.save()
    else:
        frm = MovieForm(instance=instance)
    return render(request, 'create.html',{'frm':frm })
    

def delete(request,pk):
    instance = Movieinfo.objects.get(pk=pk)
    instance.delete()
    return render(request,'edit.html')

