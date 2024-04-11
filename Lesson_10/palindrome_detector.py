
def check_palindrome(user_input):
    list_letters = []
    complete_program = True
    for character in user_input.lower():
        if character.isalpha():
            list_letters.append(character)
        elif character == " ":
            continue
        elif character == "-":
            continue
        else:
            return("\nYour input contains non-alphabetic characters\nPlease try again")
            complete_program = False # Does not complete program if user input contains numbers or punctuation characters
            break
    if list_letters == []:
        return("\nPlease enter a word or phrase")
        complete_program = False # Does not complete program if list is empty
    if complete_program:
        original_order = "".join(list_letters)
        list_letters.reverse()
        reverse_order = "".join(list_letters)
        if original_order == reverse_order:
            return(f"\nYes - '{user_input}' is a palindrome!\n")
        else:
            return(f"\n'{user_input}' is not a palindrome\nTry again!")
        