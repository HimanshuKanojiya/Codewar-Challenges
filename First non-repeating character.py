"""
First non-repeating character.
"""

def first_non_repeating_letter(string):
    total_count = ""
    for characters in string:
        if string.lower().count(characters.lower()) == 1 and len(total_count) == 0:
            total_count = total_count + str(characters)
        else:
            continue

    return total_count
