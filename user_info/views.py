from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm


# Головна сторінка
@login_required
def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")

# Реєстрація користувача
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # TODO: Зашифрувати дані та приховати їх у зображенні
            # encrypted_data = encrypt_and_hide(username, password)
            # save_to_image(encrypted_data, 'path/to/output/image.png')

            return HttpResponse("Registration successful! Your data is securely hidden.")
    else:
        form = RegistrationForm()
    return render(request, 'user_info/register.html', {'form': form})

# Логін користувача
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # TODO: Зчитати дані із прихованого зображення та розшифрувати
            # extracted_data = extract_and_decrypt('path/to/stored/image.png')
            # if validate_credentials(username, password, extracted_data):
            #     user = authenticate(username=username, password=password)  # Імітація

            user = authenticate(username=username, password=password)  # Заглушка для логіки
            if user:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, 'user_info/login.html', {'form': form})
