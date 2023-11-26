#!/usr/bin/python3

def text_indentation(text):
    """Indent text based on delimiters (?, :, .)

    Args:
        text (str): Input text to be formatted

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in "?:.":
        text = (delimiter + "\n\n").join(
            [sentence.strip(" ") for sentence in text.split(delimiter)])

    print(text)
