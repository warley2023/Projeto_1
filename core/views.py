from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


user = User.objects.create_user(username="Admin", password="123456", email="Admin@email.com")
user.save()

def minha_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("Usuário autenticado!")
            return redirect("home")
        else:
            print("Usuário ou senha inválidos.")
            return render(request, "login.html", {"error": "Usuário ou senha inválidos."})

    return render(request, "login.html")

    