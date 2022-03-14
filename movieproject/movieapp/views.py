from django.shortcuts import render, redirect

# Create your views here.
from movieapp.forms import movieforms
from movieapp.models import movie


def index(request):
    mlist = movie.objects.all()
    return render(request, 'index.html', {'mlist': mlist})


def detail(request, movie_id):
    mlist = movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'mlist': mlist})

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        desc=request.POST['desc']
        year=request.POST['year']
        img=request.FILES['img']
        movies=movie(name=name,desc=desc,year=year,img=img)
        movies.save()
        return redirect('/')
    return render(request,'add.html')


def update(request,id):
    mlist=movie.objects.get(id=id)
    form=movieforms(request.POST or None,request.FILES,instance=mlist)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':mlist})

def delete(request,id):
    if request.method=='POST':
        mlist=movie.objects.get(id=id)
        mlist.delete()
        return redirect('/')
    return render(request,'delete.html')




