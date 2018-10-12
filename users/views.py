from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'You are successfully registered as {username}!')
            return redirect('users:login_user')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    template = 'users/register_user.html'
    return render(request, template, context)


@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)      # instance=request.user | to pre-populate the form
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your profiles details were successfully updated!')
            return redirect('users:user_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)  # instance=request.user | to pre-populate the form
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form}
    template = 'users/profile.html'
    return render(request, template, context)
