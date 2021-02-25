# python ocr_form.py --image scans/full_antrag-1.png --template template/antrag-1.png
from .align_image import align_images
import imutils
import cv2
import os
from .recognition import recognize
from .file_conventer import file_converter
from .data_handler import to_pure_dict
from .file_saver import file_saver, rules
from .config import OCR_LOCATIONS, file_formats_to_save_names, ROOT_DIR, ORC_second_page
from .reader import reader


def run(
        par_template_file: str,
        par_image_file: str,
        par_locations: list,
        debug_align: bool = False,
        debug_output: bool = False,
        file_format_to_save: str = None,
        **kwargs
):
    print("[INFO] loading images...")
    image = reader.read_image(par_image_file)
    template = reader.read_template(par_template_file)

    # ------------------ align
    print("[INFO] aligning images...")
    aligned = align_images(image, template, debug=debug_align)

    print("[INFO] OCR'ing document")
    results = recognize(par_locations, aligned)
    print(results)
    # --------------- handling
    handled_data = to_pure_dict(results)
    # -------------- writing to the file
    if file_format_to_save:
        try:
            save_method = rules.get(file_format_to_save)
            save_method(data=handled_data, **kwargs)
        except KeyError:
            print(f"Method to save file for {file_format_to_save} doesn't exist")

    if debug_output:
        cv2.imshow("Input", imutils.resize(image, width=500))
        cv2.imshow("Output", imutils.resize(aligned, width=500))
        cv2.waitKey(0)
    return handled_data


if __name__ == '__main__':
    template_name = os.path.join(ROOT_DIR, 'template', 'antrag-1.png')
    image_name = os.path.join(ROOT_DIR, 'scans', 'photo11.jpg')
    location = OCR_LOCATIONS

    run(
        par_template_file=template_name,
        par_image_file=image_name,
        par_locations=location,
        debug=True,
        file_format_to_save='json',
    )
