import os
import tempfile
from io import BytesIO
import cv2
import numpy as np
from django.core.files import File
from pdf2image import convert_from_bytes


class Reader:

    def read_image(self, image_file: File):
        if self.__get_file_format(image_file) == 'pdf':
            return self.__read_pdf_file(image_file.file)
        return self.__read_cv2_file_from_inmemory_file(image_file)

    def read_template(self, template_file: File) -> np.array:
        # next line for local storage
        if os.environ.get('ICR_LOCAL_RUN'):
            template = cv2.imread(template_file.name)
        # next line for S3 bucket
        else:
            template = self.__read_cv2_file_from_inmemory_file(template_file)
        return template

    def __read_cv2_file_from_local_file(self, filename: str) -> np.ndarray:
        return cv2.imread(filename)

    def __read_cv2_file_from_filename(self, filename: str) -> np.array:
        fd = open(filename, encoding='utf8')
        img_str = fd.read()
        fd.close()
        return self.__from_str_to_numpy_arr(img_str)

    def __read_cv2_file_from_inmemory_file(self, file) -> np.array:
        img_str = file.read()
        file.close()
        return self.__from_str_to_numpy_arr(img_str)

    def __from_str_to_numpy_arr(self, _from: str, array_dtype_to=np.uint8,
                                cv2_decode_flag=cv2.IMREAD_COLOR) -> np.array:
        nparr_file = np.fromstring(_from, array_dtype_to)
        img_np = cv2.imdecode(nparr_file, cv2_decode_flag)
        return img_np

    def __read_pdf_file(self, pdf_file: BytesIO) -> np.array:
        with tempfile.TemporaryDirectory() as path:
            image_file = convert_from_bytes(pdf_file.read(), output_folder=path)[0]
            return self.__read_cv2_file_from_local_file(image_file.filename)

    def __get_file_format(self, file):
        return file.name.split('.')[-1]


reader = Reader()
