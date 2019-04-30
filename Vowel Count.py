def getCount(inputStr):
    num_vowels = 0
    vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}

    for items in vowels.keys():
        score = inputStr.count(items)
        vowels[items] = score

    for items, value in vowels.items():
        values = num_vowels
        num_vowels = values + value
    
    return num_vowels
