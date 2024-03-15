def counting_vowels(user_input):
    
    vowel_count = 0
    
    user_input_lower = user_input.lower()
    
    for character in user_input_lower:
        if character == "a" or character == "e" or character == "i" or character =="o" or character =="u":
            vowel_count = vowel_count + 1
        else:
            continue
    
    print_statements = {0:"no vowels", 1:"one vowel", 2:"two vowels", 3:"three vowels", 4:"four vowels", 5:"five vowels", 6:"six vowels", 7:"seven vowels", 8:"eight vowels", 9:"nine vowels"}
    
    if vowel_count < 10:
        number_of_vowels = print_statements[vowel_count]
    else:
        number_of_vowels = str(vowel_count) + " vowels"
    
    print(f"There are {number_of_vowels} in '{user_input}'")
