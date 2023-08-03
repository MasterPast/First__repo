result = None
operand = None
operand2 = None
operator = None
wait_for_number = True
wait_for_number2 = True
wait_for_oper = True
s = True
count = 1

while s:
    wait_for_number = True
    wait_for_oper = True
    wait_for_number2 = True
    temp = None
    print(count)
    print(wait_for_number)

    if operand == "=":
        break
    
    while wait_for_number:            
        try:
            operand = int(input('Number >>>'))
        except ValueError:
            print (operand)
            print(f'{operand} is not a number. Try again')
            print(f'you enter {operand}')
        else:
            print(f'you enter {operand}')
            if operator == None:
                result = operand
            else:
                if operator == '+':
                    result = result + operand
                elif operator == '-':
                    result = result - operand
                elif operator == '*':
                    result = result * operand
                else:
                    result = result / operand
            wait_for_number = False
        print(f'Result {result}') 

    if operand == "=":
        break

# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
    
    while wait_for_oper:
        operator = input('Operation >>>')
        print(f'you enter operator {operator}')
        if operator == "=":
            s = False
            break
        if operator != '+' and operator != '-' and operator != '*' and operator != '/':
            print('ReEnter')
        else:
            wait_for_oper = False
            
    
    print(f'So, {result}')
    # operand = input('>>>')
    # print(operand)
    count += 1

    # #print(result)
    

    
        
    
        