import art

#addition function
def add(num_1, num_2):
    return num_1 + num_2

#subtraction function
def subtract(num_1, num_2):
    return num_1 - num_2

#multiply
def multiply(num_1, num_2):
    return num_1 * num_2

#divide
def divide(num_1, num_2):
    return num_1 / num_2

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number? \n"))

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    for operator in operations:
        print(operator)

    end_program = True

    while end_program:
        operation_symbol = input("Pick an operation from the line above: \n")
        num2 = float(input("What's the next number? \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        if input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation.:') == "y":
            num1 = answer
        else:
            end_program = False
            def clear(): os.system('cls') #on Windows System
            clear()
            calculator()

calculator()