#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    skip_space = False
    
    for char in text:
        if skip_space and char == ' ':
            continue
        skip_space = False
        result += char
        if char in ['.', '?', ':']:
            result += "\n\n"
            skip_space = True

    print(result.strip())
