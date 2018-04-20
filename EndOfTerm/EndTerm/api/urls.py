from django.urls import path, include
from api import views

urlpatterns = [
   path('blogs/', views.blog_list),
   path('blogs/<int:blog_id>/', views.blog_detail),

]