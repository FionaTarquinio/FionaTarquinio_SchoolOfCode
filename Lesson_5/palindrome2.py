user_input = input("Enter word or phrase:\n")
list_letters = []
for character in user_input.lower():
    if character.isalpha():
        list_letters.append(character)
    else:
        continue
original_order = "".join(list_letters)
list_letters.reverse()
reverse_order = "".join(list_letters)
if original_order == reverse_order:
   print(f"'{user_input}' is a palindrome\n")
else:
   print(f"'{user_input}' is not a palindrome\n")