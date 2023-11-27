def romanNumber(val):
    if isinstance(val, int):
        match val:
            case _ if val >= 1000 : return "M"  + romanNumber(val -1000)            
            case _ if val >= 900  : return "CM" + romanNumber(val -900)            
            case _ if val >= 500  : return "D"  + romanNumber(val -500)            
            case _ if val >= 400  : return "CD" + romanNumber(val -400)            
            case _ if val >= 100  : return "C"  + romanNumber(val -100)
            case _ if val >= 90   : return "XC" + romanNumber(val -90)
            case _ if val >= 50   : return "L"  + romanNumber(val -50)            
            case _ if val >= 40   : return "XL" + romanNumber(val -40)            
            case _ if val >= 10   : return "X"  + romanNumber(val -10)            
            case _ if val >= 9    : return "IX" + romanNumber(val  -9)            
            case _ if val >= 5    : return "V"  + romanNumber(val  -5)            
            case _ if val >= 4    : return "IV" + romanNumber(val  -4)            
            case _ if val >= 1    : return "I"  + romanNumber(val  -1)            
            case _                : return ""
    else:    
        val = [*val] if isinstance(val, str) else val    
        match [*val]:
            case ['M', *rest]      : return 1000 + romanNumber(rest) 
            case ['C', 'M', *rest] : return 900  + romanNumber(rest) 
            case ['D', *rest]      : return 500  + romanNumber(rest) 
            case ['C', 'D', *rest] : return 400  + romanNumber(rest) 
            case ['C', *rest]      : return 100  + romanNumber(rest) 
            case ['X', 'C', *rest] : return 90   + romanNumber(rest) 
            case ['L', *rest]      : return 50   + romanNumber(rest) 
            case ['X', 'L', *rest] : return 40   + romanNumber(rest) 
            case ['X', *rest]      : return 10   + romanNumber(rest) 
            case ['I', 'X', *rest] : return 9    + romanNumber(rest) 
            case ['V', *rest]      : return 5    + romanNumber(rest) 
            case ['I', 'V', *rest] : return 4    + romanNumber(rest) 
            case ['I', *rest]      : return 1    + romanNumber(rest)
            case _                 : return 0  