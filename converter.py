import pytesseract
from PIL import Image


def conversion(image):
    pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'   

    img = Image.open(image)

    # converts the image to result and saves it into result variable 
    result = pytesseract.image_to_string(img)

    return result