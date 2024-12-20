from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_customer = True
            user.save(commit=True)
            messages.success(request, "Registration was successful.")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Something went wrong.")
            return redirect('register')
    else:
        form = UserRegisterForm()
        return render(request, 'Register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('user_profile', user_id=user.id)
            else:
                messages.error(request, "Your account is inactive.")

        else:
            messages.error(request, "The username or password is incorrect.")
        return redirect('login')
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required()
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, isinstance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated.')
        return render(request, 'EditUserProfile.html', {'from': form, 'user': user})

    return render(request, 'UserProfile.html', {'user': request.user})


@login_required()
def edit_user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exclude(pk=user.pk).exists():
            messages.error(request, "This username is already in use.")
            return render(request, "EditUserProfile.html", {"user": user})

        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            messages.error(request, "This email is already in use.")
            return render(request, "EditUserProfile.html", {"user": user})

        user.username = username
        user.email = email
        user.save()
        messages.success(request, "Your profile has been edited successfully.")
        return redirect('user_profile', user_id=user.id)

    return render(request, "EditUserProfile.html", {"user": user})
