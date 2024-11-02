from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Cuenta creada para {username}!")
            return redirect(
                "accounts:login"
            ) 
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})