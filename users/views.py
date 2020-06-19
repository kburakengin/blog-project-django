from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Post
from .forms import UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check Password Match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    password=password, email=email)

                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            # Show error message
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'users/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    else:
        return redirect('index')


@login_required
def profile(request):
    user_post = Post.objects.order_by('-date_posted').filter(author_id=request.user.id)

    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'user_post': user_post,
        'u_form': u_form,
        'p_form': p_form,

    }

    return render(request, 'users/profile.html', context)


def update_profile(request):
    user = User.objects.all().filter(id=request.user.id).first()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'user': user
        }

    return render(request, 'users/update_profile.html', context)
