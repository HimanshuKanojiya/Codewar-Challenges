"""
WeIrD StRiNg CaSe
"""
def to_weird_case(string):
    final_words = []
    process_words = []
    string_conv = []
    string = string + " "
    for runs in range(len(string)):
        if string[runs] != str(" ") or runs == 0:
            process_words.append(string[runs])
            
        elif string[runs] == str(' '):
            add = "".join(process_words)
            final_words.append(add)
            del process_words[:]

    for content_in in final_words:
        for items in range(len(content_in)):
            if items % 2 == 0:
                process_words.append(content_in[items].upper())
                
            else:
                process_words.append(content_in[items])

        string_conv.append("".join(process_words))
        del process_words[:]


    return " ".join(string_conv)
