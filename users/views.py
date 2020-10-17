from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserUpdateForm


def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'user': request.user,
        'form': form
    }

    return render(request, 'users/profile.html', context)