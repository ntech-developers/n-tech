from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignUpForm
from .forms import UserUpdateForm, ProfileUpdateForm


def registration_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # hard refresh load the profile instance created by the signal
            user.profile.language = form.cleaned_data.get('language')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.skill_level = form.cleaned_data.get('skill_level')
            user.profile.institution = form.cleaned_data.get('institution')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.country = form.cleaned_data.get('country')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('Info:home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required  # the user must be logged in
def profile(request):

    if request.method == 'POST':
        u_form = SignUpForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user)
       
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
        

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'profile.html', context)
