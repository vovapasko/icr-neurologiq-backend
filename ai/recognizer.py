from abc import ABC, abstractmethod
import platform
import pytesseract
from PIL import Image
import numpy
from google.cloud import vision


class AbstractRecognizer(ABC):
    @abstractmethod
    def recognize(self, arr: numpy.array) -> str:
        pass


class PyTesseractRecognizer(AbstractRecognizer):

    def recognize(self, arr: numpy.array) -> str:
        self._set_pytesseract()
        text = pytesseract.image_to_string(arr)
        return text

    def _set_pytesseract(self):

        if platform.system() == 'Windows':
            pytesseract.pytesseract.tesseract_cmd = r"full path to the exe file"
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        else:
            import os
            if not os.environ.get('ICR_LOCAL_RUN'):
                pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"


class GoogleVisionRecognizer(AbstractRecognizer):

    def recognize(self, arr: numpy.array) -> str:
        image = self._get_image_from_arr(arr)
        client = vision.ImageAnnotatorClient()
        response = client.text_detection(image=image)
        if response.error.message:
            print(response.error)
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        result = response.text_annotations[0].description
        return result

    def _get_image_from_arr(self, arr: numpy.array) -> vision.Image:
        tmp_img = Image.fromarray(arr)
        tmp_bytes = tmp_img.tobytes()
        image = vision.Image()
        image.content = tmp_bytes
        return image
