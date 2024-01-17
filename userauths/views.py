from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully")

            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            
            if user is not None:
                login(request, user)
                return redirect('base.home')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exists")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You're now logged in")

            return redirect('/')
        else:
            messages.warning(request, "User doesn't exist, Create an account")

    context = {

    }

    return render(request, "auth/login.html", context)