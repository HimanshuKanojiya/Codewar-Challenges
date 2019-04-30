def rgb(r, g, b):
    hex_list = [r,g,b]
    final_hex = []
    
    for items in hex_list:
    
        if items <= 255 and items >= 16:
            string = str(hex(items)).upper()
            fx =  string[2:]
            final_hex.append(fx)

        elif items < 0:
            string = str(hex(0)).upper()
            fx =  str("0") + str(string[2:])
            final_hex.append(fx)

        elif items > 255:
            string = str(hex(255)).upper()
            fx =  string[2:]
            final_hex.append(fx)
            
        elif items >= 0 and items <= 15:
            string = str(hex(items)).upper()
            fx =  str("0") + string[2:]
            final_hex.append(fx)

    return str(final_hex[0]) + str(final_hex[1]) + str(final_hex[2])
