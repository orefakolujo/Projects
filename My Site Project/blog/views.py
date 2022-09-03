from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
# Create your views here.


def index(request):
    latest_posts = Post.objects.all().order_by("date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all = Post.objects.all().order_by("date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, "blog/post-detail.html", {
        "title": identified_post.title,
        "author": identified_post.author,
        "excerpt": identified_post.excerpt,
        "image_name": identified_post.image_name,
        "date": identified_post.date,
        "content": identified_post.content,
        "tag": identified_post.tag.all(),
    })
