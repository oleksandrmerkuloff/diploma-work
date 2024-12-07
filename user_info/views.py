from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms

# Форма реєстрації
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

# Форма логіну
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

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
    return render(request, 'register.html', {'form': form})

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
    return render(request, 'login.html', {'form': form})
