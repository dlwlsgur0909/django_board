from django.shortcuts import render
import pdfplumber
# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        pdf = request.FILES.get("pdf")
        if pdf:
            context.update({
                'con' : plum_daldal(pdf)
            })
            return render(request, "pdfread/index.html", context=context)
    return render(request, "pdfread/index.html")


def plum_daldal(filename):
    text = ""
    with pdfplumber.open(filename) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text += page.extract_text()
    return text
