from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def posts(request):
    response = []
    posts = Post.objects.filter().order_by('-datetime')
    for post in posts:
        response.append(
            {
                'datetime': post.datetime,
                'content': post.content,
                'author': f"{post.user.name} {post.user.surname}"
            }
        )
    return JsonResponse(response)
