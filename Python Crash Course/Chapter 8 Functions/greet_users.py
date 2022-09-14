def greet_user(names):
    """Print a greeting to each user using a list"""
    for name in names:
        message = f'Hello, {name.title()}'
        print(message)

username = ['hanna', 'david', 'liz']
greet_user(username)