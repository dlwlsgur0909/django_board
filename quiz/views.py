from django.shortcuts import redirect, render
from .models import Quiz
from acc.models import User
import os

# Create your views here.

def index(request):
    q = Quiz.objects.all()
    u = User.objects.all().order_by("-point")
    context = {
        'con' : q,
        'u' : u
    }
    return render(request, "quiz/index.html", context=context)

def 판단(답, 제출한답, 문제번호):
    if 문제번호 == 3:
        f = open("test.py", "w")
        f.write(제출한답)
        f.close()
        if 답 == os.popen("python test.py").read().strip():
            return True
    else:
        if 답 == 제출한답:
            return True

def judge(request, conid):
    q = Quiz.objects.get(id=conid)
    ans = request.POST.get("ans")

    if 판단(q.answer, ans, int(conid)):
        u = User.objects.get(username=request.user.username)
        if not u in q.solver.all():
            q.solver.add(request.user)
            u.point += q.point
            u.save()
    return redirect("quiz:index")