from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get Form Values
        name = request.POST['name']
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
                    user = User.objects.create_user(name=name, username=username, password=password, email=email)

                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            # Show error message
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'users/register.html')
