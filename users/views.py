from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm


# Create your views here.
@login_required()
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, isinstance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated.')
        return render(request, 'EditUserProfile.html', {'from': form, 'user': user})
    else:
        return render(request, 'UserProfile.html', {'user': request.user})
