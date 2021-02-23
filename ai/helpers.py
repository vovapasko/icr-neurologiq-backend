from .config import ascii_index_to_check


def cleanup_text(text):
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()


def ignore_line(text: str):
    # if text completely contains characters, which ascii code is lower then ascii_index_to_check,
    # return False. Using this method we can throw out such a strings line '\n' or '\f'
    return all(value is True for value in [ord(char) < ascii_index_to_check for char in text])
