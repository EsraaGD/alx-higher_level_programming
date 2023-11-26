#!/usr/bin/python3
    """Define function"""
    
    
def text_indentation(text):
    """Print the text with 2 lines after '.', '?', ':'.

    Args:
        text (str): Input text to be formatted

    Raises:
        TypeError: If input text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    gonew_line = ['.', '?', ':']
    formatted_text = ""
    
    for char in text:
        formatted_text += char
        if char in gonew_line:
            formatted_text += '\n\n'
            
    for line in formatted_text.split('\n'):
        print(line.strip())