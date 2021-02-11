import cv2
import numpy as np


class FileConverter:
    def read_cv2_file_from_filename(self, filename: str) -> np.ndarray:
        return cv2.imread(filename)

    def get_cv2_file_from_file(self, filename: str) -> np.ndarray:
        fd = open(filename, encoding='utf8')
        img_str = fd.read()
        fd.close()

        # CV2
        nparr = np.fromstring(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img_np

    def get_cv2_file_from_buffer(self, buffer) -> np.array:
        img_str = buffer.read()
        buffer.close()

        # CV2
        nparr = np.fromstring(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img_np


file_converter = FileConverter()