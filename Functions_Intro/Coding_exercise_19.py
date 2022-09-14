def sum_numbers(*add:float)->float:
    """
    adds together a group of numbers
    :param sum:
    :return: float
    """
    result = 0
    for number in add:
        result += number
    return result

print(sum_numbers(8,20,2))