from django.contrib.auth import get_user_model, login as log_in, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect

User = get_user_model()

@login_required(login_url='/login/')   #login_url='/login/'
def user_list(request):
    """
    NOTE: This is fine for demonstration purposes, but this should be
    refactored before we deploy this app to production.
    Imagine how 100,000 users logging in and out of our app would affect
    the performance of this code!
    """
    users = User.objects.select_related('logged_in_user')
    print("users = ",users)
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'user_list.html', {'users': users})


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            log_in(request, form.get_user())
            return redirect(reverse("userlist"))
        else:
            print(form.errors)
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect(reverse('login'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            print(form.errors)
    return render(request, 'signup.html', {'form': form})
