##  Find all occurrences of a word

import re

    
def test1a():
    text = "asdesadp"
    pattern = r'[pea]'

    matches = re.findall(pattern, text)
    print(matches)

def test1b():
    text = "asdesadp"
    pattern = r'pea'

    matches = re.findall(pattern, text)
    print(matches)
    
def test2():
    text = "this is number 32432442"
    pattern = r'[a-z]'

    matches = re.findall(pattern, text)
    print(matches)


def test3():
    text = "There are 3 cats, 4 dogs, and 5 birds."
    pattern = r'\d'

    matches = re.findall(pattern, text)
    print(matches)


def test4():
    text = "Please contact us at support123@example.com, sales@example.com, or info@example.com."
    pattern = r'[A-Za-z0-9]'

    matches = re.findall(pattern, text)
    print(matches)


def test5():
    text = "The rain in Spain stays mainly in the plain."

    #\b asserts a word boundary.
    #\w* matches zero or more word characters (letters, digits, and underscores).
    #ain matches the literal string "ain".
    pattern = r'\b\w*ain\b'

    matches = re.findall(pattern, text)
    print(matches)


test4()