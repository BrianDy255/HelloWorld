def palindrome_sentence(sentence):
    return sentence[::].replace(" ", "").casefold() == sentence[::-1].replace(" ", "").casefold()

sentence = input("enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("Is a sentence palindrome")
else:
    print("not a palindrome")