import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change color, etc

    :param text: The text to print
    :param effects: The effect you want. One of the constants defined
    at the start of this module.
    """
    effect_string = "".join(effects)
    output_string = f'{effect_string} {text} {RESET}'
    print(output_string)


colorama.init()
color_print('Hello World', RED)
color_print('Hello World', RED,BOLD,UNDERLINE,REVERSE)
print("This should be the default terminal colour")
color_print("Hello, Blue", BLUE)
color_print("Hello, Yellow", YELLOW)
color_print("Hello, BOLD", BOLD)
color_print("Hello, underline", UNDERLINE)
color_print("Hello, reverse", REVERSE)
print("hi")
colorama.deinit()