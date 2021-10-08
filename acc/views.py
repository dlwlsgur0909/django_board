from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    messages.error(request, "에러발생!!")
    messages.success(request, "회원가입완료!")
    messages.warning(request, "경고!")
    messages.info(request, "사진없음")
    return render(request, "index.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print(dir(request))
            return redirect("acc:index")
    return render(request, "acc/login.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if User.objects.filter(username=username):
            messages.error(request, "이미 존재하는 아이디입니다")
            print("error")
            return redirect("acc:signup_user")
        password = request.POST.get('password')
        nickname = request.POST.get('nickname')
        comment = request.POST.get('comment')
        userpic = request.FILES.get('userpic')
        if not userpic:
            userpic = "no.png"
            messages.info(request, "사진이 기본값입니다 '정보수정에서 사진을 변경해주세요'")
       
            User.objects.create_user(username=username, password=password, nickname=nickname, comment=comment, userpic=userpic).save()
        return redirect("acc:login_user")
    return render(request, "acc/signup.html")

def profile_user(request):
    return render(request, "acc/profile.html")

def update(request):
    user = request.user.username
    u = User.objects.get(username=request.user.username)
    if request.method == "POST":
        p = request.POST.get("password")
        if p:
            u.set_password(request.POST.get("password"))
        u.nickname = request.POST.get("nickname")
        u.comment = request.POST.get("comment")
        up = request.FILES.get("userpic")
        if up:
            u.userpic = up
        u.save()
        user_auth = authenticate(username=user, password=p)
        login(request, user_auth)
        return redirect("acc:profile_user")

    return render(request, "acc/update.html")

def delete(request):
    User.objects.get(username=request.user.username).delete()
    return redirect("acc:login_user")

def assign(request):
    if not request.user.userpic:
        u = User.objects.get(username=request.user.username)
        u.userpic = "no.png"
        u.save()
    return redirect("acc:index")