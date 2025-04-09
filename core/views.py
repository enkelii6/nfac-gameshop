from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    return render(request, 'core/home.html')
