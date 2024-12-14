from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': user_form})


def home(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)

    is_profile_complete = all([
        profile.first_name,
        profile.last_name,
        profile.date_of_birth,
        profile.country,
        profile.phone_number,
        profile.passport_number,
    ])

    return render(request, 'home.html', {
        'form': form,
        'is_profile_complete': is_profile_complete,
        'profile': profile
    })


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
