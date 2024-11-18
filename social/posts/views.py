from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'posts/index.html')


def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/posts.html', context)


def single_post(request, id):
    post = Post.objects.get(id=id)
    url = post.youtube_url
    if url:
        if 'watch' in url:
            url = url.replace('watch?v=', 'embed/')
        elif 'youtu.be' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0]  # Get the video ID from URL
            url = f"https://www.youtube.com/embed/{video_id}"  # Create the embed URL
        else:
            url = ''
    context = {'post': post,
               'url': url}
    return render(request, 'posts/single_post.html', context)


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Do not save yet
            post.owner = request.user  # Assign the logged-in user's name
            post.save()  # Now save the post
            return redirect('single_post', id=post.id)
    else:
        form = PostForm()  # Initialize empty form for GET request
    context = {'form': form}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url='login')
def edit_post(request, id):
    user = request.user
    posts = Post.objects.filter(owner=user)
    post = posts.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('single_post', id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form,
               'post': post}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url='login')
def delete_post(request, id):
    user = request.user
    posts = Post.objects.filter(owner=user)
    post = posts.get(id=id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('posts')
    context = {'post': post}
    return render(request, 'posts/delete_post.html', context)
