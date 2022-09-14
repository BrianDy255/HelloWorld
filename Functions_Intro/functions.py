def multiply(x: float,y: float) -> float:
    """
    Multiplies a variable `x` with the variable `y`.
    :param x: integer
    :param y: integer
    :return: result of x * y
    """
    result = x*y
    return result


def is_palendrome(string: str) -> bool:
    """
    Checks to see if a string is a palendrome
    :param string: checks string
    :return: boolean
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str)->bool:
    """
    Checks to see if a sentence string is a palindrome.
    :param sentence:
    :return: returns true or false
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palendrome(string)


# word = input("Please enter a word to check:\n")
# if palindrome_sentence(word) :
#     print(f'{word} is a palendrome')
# else:
#     print(f'{word} is not a palendrome')
#
answer = multiply(18,3)
print(answer)


def fibonacci(n: int) -> int:
    """ Return the `n` th Fibonacci number, for positive `n`. """
    if 0 <= n <=1:
        return n

    n_minus1, n_minus2 = 1,0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(36):
    print(i,fibonacci(i))