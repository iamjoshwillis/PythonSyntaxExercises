

def print_upper_words(words, starting_char):
    '''Input a list of words as separate strings; will output text in all caps'''
    '''Enter a character(s) in starting_chars list that word must start with to print'''


    for word in words:
        for letter in starting_char:
            if word.startswith(letter):
                print(word.upper())


print_upper_words(["Hello", "Goodbye", "How's it going?", "Bye"], ["H", "G"])