from django.shortcuts import render
import pytesseract
from PIL import Image

# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        f = request.FILES.get("pic")
        if not f:
            return render(request, "ocr/index.html")
        l = request.POST.get("lang")
        pytesseract.pytesseract.tesseract_cmd = 'tess/tesseract.exe'
        im = Image.open(f)
        t = pytesseract.image_to_string(im, lang=l)
        context.update({
            'con': t,
            'lang' : l
        })
        return render(request, "ocr/index.html", context=context)
    return render(request, "ocr/index.html")