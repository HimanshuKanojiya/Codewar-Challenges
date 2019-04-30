def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for items in vowels:
	    if items in string:
		    cur = string.replace(items,"") #it will replace the vowel with blank
		    string = cur #after completing the operation, it will update the current string
	    else:
		    continue #if vomel not find in string then it will continue the program
    
    return string
