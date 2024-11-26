from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Event, Event_post
from datetime import datetime
from .forms import EventForm, Event_postForm
from .tools import is_staff
from comments.models import Event_comment
from comments.forms import Event_commentForm

# Create your views here.


def events(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events.html', context=context)


def single_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.user.is_staff:
        posts = Event_post.objects.filter(event=event)
    else:
        today = datetime.today().date()
        posts = Event_post.objects.filter(event=event, available_date__lte=today)
    context = {
        'event': event,
        'posts': posts
    }
    return render(request, 'events/single_event.html', context=context)


def event_post(request, even_post_id):
    post = Event_post.objects.get(id=even_post_id)
    url = post.event_yt_url
    comments = Event_comment.objects.filter(event_post=post)
    form = Event_commentForm()
    if request.method == 'POST':
        form = Event_commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.event_post = post
            comment.save()
            return redirect('event_post', even_post_id=post.id)
    if url:
        if 'watch' in url:
            url = url.replace('watch?v=', 'embed/')
        elif 'youtu.be' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0]  # Get the video ID from URL
            url = f"https://www.youtube.com/embed/{video_id}"  # Create the embed URL
        else:
            url = ''
    context = {
        'post': post,
        'url': url,
        'form': form,
        'comments': comments
    }
    return render(request, 'events/event_post.html', context=context)


@login_required(login_url='login')
def delete_event(request, event_id):
    events = Event.objects.filter(owner=request.user)
    event = events.get(id=event_id)
    title = event.event_name
    if request.method == 'POST':
        event.delete()
    context = {
        'title': title,
        'event': event
    }
    return render(request, 'events/delete_event.html', context)


@login_required(login_url='login')
def delete_event_post(request, even_post_id):
    post = Event_post.objects.get(id=even_post_id)
    title = post.event_post_title
    if request.method == 'POST':
        post.delete()
    context = {
        'title': title,
        'post': post
    }
    return render(request, 'events/delete_event_post.html', context)


def add_event(request):
    is_staff(request, 'index')
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('events')

    context = {
        'form': form
    }
    return render(request, 'events/add_event.html', context)


def edit_event(request, event_id):
    is_staff(request, 'index')
    event = Event.objects.get(id=event_id)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')

    context = {
        'form': form
    }
    return render(request, 'events/add_event.html', context)


def create_event_post(request, event_id):
    is_staff(request, 'index')
    event = Event.objects.get(id=event_id)
    form = Event_postForm()
    if request.method == 'POST':
        form = Event_postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.event = event
            post.save()
            return redirect('events')

    context = {
        'form': form
    }
    return render(request, 'events/add_event_post.html', context)


def edit_event_post(request, post_id):
    is_staff(request, 'index')
    post = Event_post.objects.get(id=post_id)
    form = Event_postForm(instance=post)
    if request.method == 'POST':
        form = Event_postForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('events')

    context = {
            'form': form
        }
    return render(request, 'events/add_event_post.html', context)
