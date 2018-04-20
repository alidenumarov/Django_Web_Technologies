from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs_list, name="blog_list"),
    path('blogs/<int:blog_id>', views.blogs_details, name="blog_details"),
    path('blogs/create', views.blog_create, name="blog_create"),
    path('blogs/update/<int:blog_id>', views.blog_update, name="blog_update"),
    path('blogs/delete/<int:blog_id>', views.blog_delete, name="blog_delete"),
]