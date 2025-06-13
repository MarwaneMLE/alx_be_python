def safe_divide(numerator, denominator):
    try:
        if denominator != 0 and denominator is not str and numerator is not str:
            result = float(numerator) / float(denominator)
            return result
        else:
            print(f"The result of the division is {result}")
    
    except ZeroDivisionError as Exception:
        return "Error: Cannot divide by zero."
    
    except ValueError as Exception:
        return "Error: Please enter numeric values only." 
