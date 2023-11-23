from django.shortcuts import render, redirect

from django.contrib.auth import login

from .forms import SignupForm


def homepage(request):
    return render(request, 'core/homepage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})