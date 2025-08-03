from django.shortcuts import render, redirect

from blog.forms import PostForm
from .models import Post


# Create your views here.


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'posts': post_list})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect('blog:post_list')
            else:
                form.add_error(None, "Debes iniciar sesión para crear una publicación.")
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', context={'form': form})


