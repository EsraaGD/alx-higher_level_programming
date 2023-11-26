#!/usr/bin/python3

def text_indentation(text):
    """Indent text based on delimiters (?, :)"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in "?:.":
        text = (delimiter + "\n\n").join(
            [sentence.strip(" ") for sentence in text.split(delimiter)])

    print(text)
