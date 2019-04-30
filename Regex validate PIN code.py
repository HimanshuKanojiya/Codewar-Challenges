def validate_pin(pin):
    #return true or false
    if len(pin) == 4 and pin.isdigit() == True: #for checking the pin length and pin type
        return True
    elif len(pin) == 6 and pin.isdigit() == True:
        return True
    else:
        return False
      
