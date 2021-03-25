from django.core.files.base import ContentFile
import base64
import six


def from_base64_to_content_file(base64_str: str, filename: str) -> ContentFile:
    '''
    Converts base64 string to Django ContentFile named after given filename. Note that you should give filename
    without extension. Extension will be extracted from base64_str
    :param base64_str: string to convert
    :param filename: the name of the created file
    :return: Django ContentFile file
    '''
    data = base64_str
    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')
            file_format = header.split('/')[-1]
            filename += f".{file_format}"
        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_file')

        return ContentFile(decoded_file, name=filename)
