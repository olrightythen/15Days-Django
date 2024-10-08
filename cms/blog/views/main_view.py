from django.shortcuts import render,redirect,get_object_or_404
from ..models import Blog
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    blogs = Blog.objects.all()
    return render(request,"main/home.html",{"blogs":blogs})

def single_blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,"main/single_blog.html",{"blog":blog})

@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        blog = Blog(title=title,subtitle=subtitle,description=description,image=image,author=request.user)
        blog.save()
        return redirect("/blog/")

    return render(request,"main/create_blog.html")

@login_required
def edit_blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    if request.method == "POST" and blog.author == request.user:
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        blog.title = title
        blog.subtitle = subtitle
        blog.description = description
        if image:
            blog.image = image
        blog.save()
        return redirect("/blog/")
    return render(request,"main/edit_blog.html",{"blog":blog})

@login_required
def delete_blog(request,blog_id):
   if request.method == "POST":
        blog = get_object_or_404(Blog,pk=blog_id)
        if blog.author == request.user:
            blog.delete()
            return redirect("home")
        else:
            return redirect("single_blog",blog_id=blog_id)



