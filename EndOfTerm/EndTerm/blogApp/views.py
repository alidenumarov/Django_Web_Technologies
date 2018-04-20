from django.shortcuts import render
from blogApp.models import Blog
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def blogs_list(request):
    if(request.method == "GET"):
        blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {"blog_list": blogs, "active_menu": "blog"})

def blogs_details(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog/blog_details.html', {"blog": blog, "active_menu": "blog"})
    
def blog_create(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        body = request.POST['body']
        created_at = request.POST['created_at']
        blog = Blog(title = title, body = body)
        blog.save()
        return redirect('/blogs')
    return render(request, 'blog/blog_create.html', {"active_menu": "blog"})

def blog_update(request, blog_id):
    try:
        curBlog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    if(request.method == "POST"):
        curBlog.title = request.POST['title']
        curBlog.body = request.POST['body']
        created_at = request.POST['created_at']
        curBlog.save()
        return redirect('/blogs')
    return render(request, 'blog/blog_update.html', {"blog": curBlog, "active_menu": "blog"})

@csrf_exempt
def blog_delete(request, blog_id):
    try:
        curBlog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    if(request.method == "POST"):
        curBlog.delete()
        return redirect('/blogs')
    return render(request, 'blog/blog_delete.html', {"blog": curBlog, "active_menu": "blog"})