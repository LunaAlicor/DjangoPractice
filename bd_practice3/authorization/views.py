from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy


def my_login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')

        return render(request, 'authorization/login.html')
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')
    return render(request, 'authorization/login.html', {'error': "Ты инвалид"})


def set_cookie(request):
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request):
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: "+value)


def set_session_view(request):
    request.session["foobar"] = 'spameggs'
    return HttpResponse("Session set!")


def get_session_view(request):
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value}")


def logout_view(request):
    logout(request)
    return redirect(reverse("login"))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('login')
