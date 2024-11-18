from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import Custom_user_creation_form, Profile_form, Message_form
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from posts.models import Post
from django.db.models import Q
from .models import Message
import datetime


def register_user(request):
    form = Custom_user_creation_form()
    context = {'form': form}

    if request.method == 'POST':
        form = Custom_user_creation_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('index')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)

    return render(request, 'users/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return print('login')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        User = get_user_model()  # Get the custom user model

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Email does not exist')

        try:
            user = authenticate(request, username=user.username, password=password)  # Using username for authentication
            auth_login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'index')
        except:
            messages.error(request, 'Email or password is incorrect')

    return render(request, 'users/login.html')


@login_required(login_url='login')
def profile(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.profile
    form = Profile_form(instance=profile)
    if request.method == 'POST':
        form = Profile_form(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def delete_profile(request):
    user_id = request.user.id
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('index')  # Redirect to a desired location after deletion
    return render(request, 'users/confirm_delete.html', {'user': user})


def users(request):
    users = get_user_model().objects.all()
    context = {'users': users}
    return render(request, 'users/users.html', context)


def user_info(request, user_id):
    page_user = get_user_model().objects.get(id=user_id)
    posts = Post.objects.filter(owner=page_user)
    context = {'page_user': page_user,
               'posts': posts}
    return render(request, 'users/user_info.html', context)


@login_required(login_url='login')
def message(request, recipient_id):
    user = request.user
    recipient = get_user_model().objects.get(id=recipient_id)

    time_threshold = datetime.datetime.now() - datetime.timedelta(hours=72)

    Message.objects.filter(
        created__lt=time_threshold,
        sender__in=[user, recipient],
        recipient__in=[user, recipient]
    ).delete()

    if user == recipient:
        return redirect('users')

    if request.method == 'POST':
        form = Message_form(request.POST)
        if form.is_valid():
            sent_message = form.save(commit=False)
            sent_message.sender = user
            sent_message.recipient = recipient
            sent_message.save()
            return redirect('message', recipient_id)

    form = Message_form()

    website_messages = Message.objects.filter(
        Q(sender=user, recipient=recipient) | Q(sender=recipient, recipient=user)
    )

    read_message = Message.objects.filter(sender=recipient, recipient=user)
    read_message.update(is_read=True)

    sent_message_count = Message.objects.filter(
        sender=user,
        recipient=recipient,
    ).count()
    chances = 5 - sent_message_count

    context = {'recipient': recipient,
               'form': form,
               'website_messages': website_messages,
               'chances': chances}
    return render(request, 'users/message.html', context)


@login_required(login_url='login')
def message_list(request):
    user = request.user
    website_messages = Message.objects.filter(recipient=user)
    context = {'website_messages': website_messages}
    return render(request, 'users/message_list.html', context)