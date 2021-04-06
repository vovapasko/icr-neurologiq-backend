from abc import ABC, abstractmethod
import platform
import pytesseract
from PIL import Image
import numpy
from google.cloud import vision
from tempfile import TemporaryDirectory


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

    def recognize(self, arr: numpy.array, debug_name: str = None) -> str:
        '''
        Implementation of recognize method from AbstractRecognizer class using Google ICR
        :param arr: slice of main picture to recognize. Given in numpy.array
        :param debug_name: string name of picture slice. Sometimes we would like to see what
        is sent to Google ICR. That's why we may use this variable. Usually it is None.
        :return: string text what Google ICR has in picture recognized
        '''
        image = self._get_image_from_arr(arr, debug_name)
        client = vision.ImageAnnotatorClient()
        response = client.text_detection(image=image)
        if response.error.message:
            print(response.error)
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        try:
            result = response.text_annotations[0].description
        except IndexError:
            result = ''
        return result

    def _get_image_from_arr(self, arr: numpy.array, debug_name: str = None) -> vision.Image:
        tmp_img = Image.fromarray(arr)
        # for debugging purposes sometimes we need to see what image is sent to google.
        # that's why we need second if block
        if debug_name:
            tmp_img.save(f'{debug_name}.png')
        # for now only correct way to read bytes from tmp_img is to save it in temporary
        # directory and read bytes from already saved file
        with TemporaryDirectory() as td:
            filename = f"{td}/file.png"
            tmp_img.save(filename)
            with open(filename, 'rb') as tmp_file:
                tmp_bytes = tmp_file.read()
        image = vision.Image()
        image.content = tmp_bytes
        return image
