from django.shortcuts import render
from googletrans import Translator

# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        text = request.POST.get("before")
        if text:
            translator = Translator()
            f = request.POST.get("from")
            t = request.POST.get("to")
            if not f or not t:
                f = "en"
                t = "ko"
                trans = translator.translate(text, dest="ko")
            else:
                trans = translator.translate(text, src=f, dest=t)
                
            context.update({
                'after' : trans.text,
                'before' : text,
                'from' : f,
                'to' : t,
            })
    return render(request, "trans/index.html", context=context)

 

