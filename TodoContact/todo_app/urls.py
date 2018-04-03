from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books_list, name="book_list"),
    path('books/<int:book_id>', views.books_details, name="book_details"),
    
    path('authors/', views.authors_list, name="author_list"),
    path('authors/<int:author_id>', views.authors_details, name="author_details"),

    path('todos/', views.todo_list, name="todo_list"),
    path('todos/create', views.todo_create, name="todo_create"),
    path('todos/sort', views.todo_sort, name="todo_sort"),    
    path('todos/update/<int:todo_id>', views.todo_update, name="todo_update"),
    path('todos/delete/<int:todo_id>', views.todo_delete, name="todo_delete"),

    path('contacts/', views.contact_list, name="contact_list"),
]