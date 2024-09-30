from django.shortcuts import render,redirect
from ..models import Blog
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    Blogs = Blog.objects.all()
    return render(request,"main/home.html",{"Blogs":Blogs})

def single_blog(request):
    return render(request,"main/single_blog.html")

def edit_blog(request):
    return render(request,"main/edit_blog.html")

@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        blog = Blog(title=title,subtitle=subtitle,description=description,image=image)
        blog.save()
        return redirect("/blog/")

    return render(request,"main/create_blog.html")



