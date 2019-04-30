"""
Human Readable Time
"""

def make_readable(second):
    from datetime import timedelta
    conv = str(timedelta(seconds = second))

    if str("days") in str(conv):
        index = conv.index(",")
        formated = conv[index + 1:]
        first_check = formated.find(":")
        num = int(formated[:first_check]) + int(conv[:index-4]) * 24
        return str(num) + ":" + str(formated[first_check + 1:])

    elif str("day") in str(conv):
        index = conv.index(",")
        formated = conv[index+1:]
        first_check = formated.find(":")
        num  = int(formated[:first_check]) + int(conv[:index - 4]) * 24
        return str(num) + ":" + str(formated[first_check + 1:])
        
        
    else:
        if str("0") == conv[:conv.find(":")]:
            return str("0" + conv)
        else:
            for limit in range(1,10):
                if str(limit) == conv[:conv.find(":")]:
                    return str("0" + conv)

                else:
                    continue
                
            return str(conv)
    
    
