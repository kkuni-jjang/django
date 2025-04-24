from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("form.is_valid():", form.is_valid())

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                print("form.cleaned_data:", form.cleaned_data)
                return redirect("/posts/feeds/")  # 로그인 성공 후 리디렉션
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")  # 로그인 실패 처리

        context = {"form": form}
        return render(request, "users/login.html", context)

    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/users/login/")

def signup(request):
    form = SignupForm()
    context = {"form" : form}
    return render(request,"users/signup.html", context)