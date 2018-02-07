from django.shortcuts import render,redirect
from post.forms import postForm
from post.models import post
# Create your views here.

def index(request):
    title = "WELCOME PAGE | Seedstars Application"
    return render (request, 'homesite/home.html',{"title": title})


def list_post(request):
    show_post = post.objects.all()
    return render(request,"homesite/list_post.html",{"title":"Listing post","post":show_post})


def add_post(request):
    form = ""
    msg = ""
    if request.method == "POST" :
        form = postForm(request.POST)
        if form.is_valid():
            msg = "Created Successfully"
            instance = form.save(commit = False)
            instance.save()
    return render(request,"homesite/add_post.html",{"title":"Add post","form":form,"msg": msg})
