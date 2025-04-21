from django.shortcuts import render, HttpResponse, redirect
from . models import Movieinfo
from . forms import MovieForm

# Create your views here.

def create(request):
    if request.method == "POST":
        frm = MovieForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('list')  # Redirect to the list view after saving
        else:
            print("Form errors:", frm.errors)  # Optional: Debugging
    else:
        frm = MovieForm()
    return render(request, 'create.html', {'frm': frm})
    

def list(request):
    movie_data = Movieinfo.objects.all()
    return render(request, 'list.html', {'movies':movie_data})

def edit(request, pk):
    instance = Movieinfo.objects.get(pk=pk)
    if request.method == "POST":
        frm = MovieForm(request.POST, request.FILES, instance=instance)  # <- include request.FILES
        if frm.is_valid():
            frm.save()
            return redirect('list')  # Optional: Redirect to list view after update
        else:
            print("Form errors:", frm.errors)  # Debugging
    else:
        frm = MovieForm(instance=instance)
    return render(request, 'create.html', {'frm': frm})
    

def delete(request,pk):
    instance = Movieinfo.objects.get(pk=pk)
    instance.delete()
    return render(request,'edit.html')

