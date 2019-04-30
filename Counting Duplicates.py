"""
Counting Duplicates
"""
def duplicate_count(text):
    dup_count = [0]
    text = text.lower()
    for chars_in in text:
        if text.count(chars_in) == 1:
            continue    
        elif text.count(chars_in) > 1:
            dup_count[0] = dup_count[0] + 1
            text = text.replace(chars_in,"")

    return dup_count[0]
     
