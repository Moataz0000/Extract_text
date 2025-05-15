
from PIL import Image
import pytesseract
import re


class ExtractText:

    @staticmethod
    def clean_text(text: str) -> str:
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text


    @staticmethod
    def extract_text(image):
         text = pytesseract.image_to_string(Image.open(image))
         ExtractText.clean_text(text)
         return text
