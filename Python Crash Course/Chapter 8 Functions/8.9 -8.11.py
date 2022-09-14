print("exercise 8.9")
message = ['Hello', 'good morning', 'good evening']

def show_message(message):
    """Print messages from a list"""
    for text in message:
        print(f'Currently printing out {text}')

show_message(message)

print('\nExercise 8.10')

message = ['Hello', 'good morning', 'good evening']
sent_messages = []

def send_messages(message,sent_messages):
    """Popping and appending messages"""
    while message:
        current_message = message.pop()
        print(f'Currently popping {current_message}')
        sent_messages.append(current_message)

def print_message(sent_messages):
    print(f'Printing out new messages:')
    for message in sent_messages:
        print(message)

send_messages(message[:],sent_messages)
print_message(sent_messages)

print('\nExercise 8.11')

print(message)
print(sent_messages)
