def factorial(num: int)-> int:
    """
    Finds the factorial of a number n! 0! = 1
    :param num: integer
    :return: integer
    """
    if num <= 1:
        return 1

    result =2
    for x in range(3,num +1):
        result *= x

    return result

for i in range(6):
    print(i, factorial(i))