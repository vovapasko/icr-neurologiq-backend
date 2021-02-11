# ------------------ recognition
import platform
from enum import Enum
from .helpers import ignore_line
import cv2
import pytesseract


def recognize(locations, aligned_img) -> dict:
    parsingResults = []
    for loc in locations:
        (x, y, w, h) = loc.bbox
        roi = aligned_img[y:y + h, x:x + w]

        rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        set_pytesseract()
        text = pytesseract.image_to_string(rgb)
        parse_read_text(text, parsingResults, loc)
    results = {}

    for (loc, line) in parsingResults:
        r = results.get(loc.id, None)

        if r is None:
            results[loc.id] = (line, loc._asdict())
        else:
            (existingText, loc) = r
            text = "{}\n{}".format(existingText, line)

            results[loc["id"]] = (text, loc)
            print("text", text)
    return results


def set_pytesseract():
    if platform.system() == 'Windows':
        pytesseract.pytesseract.tesseract_cmd = r"full path to the exe file"
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    else:
        pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"


def parse_read_text(text: str, parsingResults: list, loc: Enum):
    for line in text.split("\n"):
        if (len(line)) == 0 or ignore_line(line):
            continue
        lower = line.lower()
        count = sum([lower.count(x) for x in loc.filter_keywords])

        if count == 0:
            parsingResults.append((loc, line))
