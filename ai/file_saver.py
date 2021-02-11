import csv
from typing import TextIO
import json

from ai.config import file_formats_to_save_names


# Don't forget to add method in rules dict below the class
class FileSaver:

    def to_csv(
            self, data: dict,
            filename: str = file_formats_to_save_names.get('csv'),
            mode: str = 'w'
    ) -> TextIO:
        print("[INFO] Converting data to csv")
        with open(filename, mode, newline='') as file:
            fieldnames = data.keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(data)
        return file

    def to_json(
            self, data: dict,
            filename: str = file_formats_to_save_names.get('json'),
            mode: str = 'w'
    ) -> TextIO:
        print("[INFO] Converting data to json")
        json_data = json.dumps(data)
        with open(filename, mode=mode) as file:
            file.write(json_data)
        return file


file_saver = FileSaver()
rules = {
    'json': file_saver.to_json,
    'csv': file_saver.to_csv
}
