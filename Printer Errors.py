def printer_error(s):
    error_string = [0]
    total_length = len(s)
    allowed_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

    for strings in s:
        if str(strings.lower()) in allowed_alpha:
            continue
        elif str(strings.lower()) not in allowed_alpha:
            cur = int(error_string[0])
            error_string[0] = int(cur) + 1

    return str(error_string[0]) + "/" + str(total_length)
