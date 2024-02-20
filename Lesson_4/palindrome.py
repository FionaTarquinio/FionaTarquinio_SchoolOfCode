input_word = input("Enter your word:\n")
list_letters = list(input_word.lower())
list_letters.reverse()
input_word_reversed = "".join(list_letters)
is_palindrome = input_word.lower() == input_word_reversed
if is_palindrome == True:
   print(f"Your word, '{input_word}', is a palindrome\n")
else:
   print(f"Your word, '{input_word}', is not a palindrome\n")