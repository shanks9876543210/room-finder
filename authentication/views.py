from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def register_success(request):
    return render(request, 'register_success.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('room_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# def staff_login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_staff:
#                 auth_login(request, user)
#                 return redirect('room_list')
#             else:
#                 form.add_error(None, "You do not have staff access.")
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'staff_login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')
