import pytesseract
from PIL import Image



pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'   

img = Image.open('sample.png')

# converts the image to result and saves it into result variable 
result = pytesseract.image_to_string(img)

print(result)