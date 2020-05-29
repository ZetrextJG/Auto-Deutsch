import cv2
import pytesseract
import os


def image_to_text(name):
    pytesseract.pytesseract.tessercat_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(f'temp/{name}.png')
    text = pytesseract.image_to_string(img, lang="eng")

    try:
        standart_path = os.getcwd()
        os.remove(f"{standart_path}\\temp\\{name}.png")
    except Exception as ex:
        print(ex)

    return text