from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import Blog
from api.serializers import BlogSerializer

@csrf_exempt
def blog_list(request):
    if(request.method == "GET"):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == "POST"):
        blogToAdd = request.POST
        serializer = BlogSerializer(data=blogToAdd)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    if(request.method == "GET"):
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data)
        blog.delete()
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data)
    elif(request.method == "PUT"):
        curBlog = JSONParser().parse(request)
        curBlog = request.POST
        blog.title = curBlog.get('title', '')
        blog.body = curBlog.get('body', '')        
        blog.save()
        return JsonResponse(serializer.errors)
        serializer = BlogSerializer(blog, curBlog)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif(request.method == "DELETE"):
        blog.delete()
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data)
