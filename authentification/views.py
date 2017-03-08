from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        return render(request, 'authentification/login.html', {'error_message': 'НЕВЕРНО ВВЕДЕНЫ ДАННЫЕ'})
    return render(request, 'authentification/login.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.save()
        except:
            return render(request, 'authentification/registration.html', {'error_message': 'НЕ УДАЛОСЬ ЗАРЕГИСТРИРОВАТЬ АККАУНТ. ПОЖАЛУЙСТА, ПОВТОРИТЕ ПОПЫТКУ'})

        if user is not None:
            if user.is_active:
                login(request, user)

    return render(request, 'authentification/registration.html')

def logout_user(request):
    logout(request)
    return render(request, 'authentification/login.html')