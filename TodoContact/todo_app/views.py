from django.shortcuts import render, redirect
from todo_app.models import Book, Author, Todo, Contact
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def todo_list(request):
    if(request.method == "GET"):
        todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {"todo_list": todos, "active_menu": "todo"})

def todo_create(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        todo = Todo(title = title, description = description)
        todo.save()
        return redirect('/todos')
    return render(request, 'todo/todo_create.html', {"active_menu": "todo"})

def todo_update(request, todo_id):
    try:
        curTodo = Todo.objects.get(pk=todo_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    if(request.method == "POST"):
        curTodo.title = request.POST['title']
        curTodo.description = request.POST['description']
        curTodo.priority = request.POST['priority']
        curTodo.save()
        return redirect('/todos')
    return render(request, 'todo/todo_update.html', {"todo": curTodo, "active_menu": "todo"})

def todo_sort(request):
    if(request.method == "GET"):
        sortedTodos = Todo.objects.all().order_by('priority')
    return render(request, 'todo/todo_sort.html', {"todo_list": sortedTodos, "active_menu": "todo"})

@csrf_exempt
def todo_delete(request, todo_id):
    try:
        curTodo = Todo.objects.get(pk=todo_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    if(request.method == "POST"):
        curTodo.delete()
        return redirect('/todos')
    return render(request, 'todo/todo_delete.html', {"todo": curTodo, "active_menu": "todo"})

def contact_list(request):
    contacts = Contact.objects.all()
    query = request.GET.get("q")
    if query:
        contacts = contacts.filter(name__icontains=query)
    return render(request, 'contact/contact_list.html', {"contact_list": contacts, "active_menu": "contact"})

def index(request):
    return render(request, 'index.html')

def books_list(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'book/book_list.html', {"book_list": books, "active_menu": "book"})


def books_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book/book_details.html', {"book": book, "active_menu": "book"})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {"author_list": authors, "active_menu": "author"})


def authors_details(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'author/author_details.html', {"author": author, "active_menu": "author"})