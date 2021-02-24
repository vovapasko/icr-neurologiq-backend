from pdf2image import convert_from_path

from ai.file_conventer import file_converter
import tempfile

with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path('Beitrittserklärung.pdf', output_folder=path)
    b = file_converter.read_cv2_file_from_filename(images_from_path[0].filename)
    print(b)
