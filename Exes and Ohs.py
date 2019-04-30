def xo(s):
    s = s.lower()
    
    if str("x") in s and str("o") in s and len(s) != 0:
        x_count = s.count("x")
        o_count = s.count("o")
        
        if x_count == o_count:
            return True
            
        elif x_count != o_count:
            return False
            
    elif (str("x") not in s and str("o") not in s) and (len(s) != 0 or len(s) == 0):
        return True
