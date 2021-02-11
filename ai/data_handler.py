import cv2.cv2 as cv2
from typing import Dict, Tuple
from ai.helpers import cleanup_text


def to_columns_list(data: Dict, aligned) -> list:
    columns = []
    for (locID, result) in data.items():
        (text, loc) = result
        print(loc["id"])
        print("=" * len(loc["id"]))
        print("{}\n\n".format(text))

        (x, y, w, h) = loc["bbox"]
        clean = cleanup_text(text)
        columns.append(clean)
        cv2.rectangle(aligned, (x, y), (x + w, y + h), (0, 255, 0), 2)

        for (i, line) in enumerate(text.split("\n")):
            startY = y + (i * 70) + 40
            cv2.putText(aligned, line, (x, startY), cv2.FONT_HERSHEY_SIMPLEX, 1, (102, 102, 255), 2)
    return columns


def to_pure_dict(data: dict) -> dict:
    new_dict = {}
    for key in data.keys():
        new_dict.update({key: data.get(key)[0]})
    return new_dict
