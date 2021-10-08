import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'tess/tesseract.exe'
im = Image.open("베트남.png")
text = pytesseract.image_to_string(im, lang="vie")
print(text)

