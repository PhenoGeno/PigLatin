vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "S", "T", "V", "X", "Z", "H", "R", "W", "Y", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

word = input('Translate to Piglatin: ')
letter = word[0]
if letter in consonants:
    first_letter_replaced = word.replace(word[0], '', 1)
    last_letter_replaced = first_letter_replaced + word[0]
    finished = last_letter_replaced + 'ay'
    print(finished.lower())
elif letter in vowels:
    vowel_finished = word + "yay"
    print(vowel_finished.lower())
else:
    print("There was an error")