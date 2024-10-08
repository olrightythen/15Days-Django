from django.urls import path
from .views.main_view import home,create_blog,single_blog,edit_blog,delete_blog
from .views.auth_view import register,login

urlpatterns = [
    path("",home, name="home"), 
    path("register/",register, name="register"), 
    path("login/",login, name="login"), 
    path("create/",create_blog, name="create_blog"), 
    path("<int:blog_id>/",single_blog, name="single_blog"),
    path("edit/<int:blog_id>/~",edit_blog, name="edit_blog"),
    path("delete/<int:blog_id>/",delete_blog, name="delete_blog"),
]