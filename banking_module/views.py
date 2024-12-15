from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile, BankClient
from .utils import aes256_encryption as aes
from .utils.image_gen import new_image
from .utils.steganography import decode_lsb, encode_lsb


SIMPLE_IMAGES = r'D:\Oleksandr\Диплом\third chapter\project\diploma_platform\banking_module\static\banking_module\images\simple'
_image = r'D:\Oleksandr\Диплом\third chapter\project\diploma_platform\banking_module\static\banking_module\images\hidden'


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            BankClient.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'banking_module/register.html', {'form': user_form})



@login_required
def home(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    # Якщо профіль порожній (новий користувач)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():

            #! aes 256 modules
            # passphrase = "securepassword123"
            # user_data = '\n'.join([
            #     f'First name: {profile.first_name}',
            #      f'Last name: {profile.last_name}',
            #     f'Date of birth: {str(profile.date_of_birth)}',
            #     f'Country: {profile.country}',
            #     f'Phone: {profile.phone_number}',
            #     f'Passport: {profile.passport_number}',
            #     ])
            # print(user_data)

            # encrypted_data = aes.aes_encrypt(user_data, passphrase)
            # print(encrypted_data)

            # decrypted_data = aes.aes_decrypt(encrypted_data, passphrase)
            # print(decrypted_data)

            #! donwload image
            # image = new_image()
            # image_path = f'{SIMPLE_IMAGES}\\{113}.jpg'
            # with open(image_path, 'wb') as file:
            #     file.write(image)

            #! STEGO
            # encode_lsb(image_path, f'{_image}\\113.jpg', 'Hello world!')
            print(decode_lsb(f'{_image}\\113.jpg'))

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

    return render(request, 'banking_module/home.html', {
        'form': form,
        'is_profile_complete': is_profile_complete,
        'profile': profile
    })


class CustomLoginView(LoginView):
    template_name = 'banking_module/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
