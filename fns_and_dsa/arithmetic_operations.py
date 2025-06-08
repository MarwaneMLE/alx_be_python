def perform_operation(num1, num2, operation):
    try :
        match operation:
            case 'add':
                result = num1 + num2
            
            case 'subtract':
                result = num1 - num2

            case 'multiply':
                result = num1 * num2

            case 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division By Zero!!!!")   
        return result  
    except: 
        print("Enter correct operation")
