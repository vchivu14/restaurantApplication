from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserRegisterForm, UserUpdateForm
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('users:login'))
    context = {
        "user": request.user
    }
    return render(request, "users/profile.html", context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})