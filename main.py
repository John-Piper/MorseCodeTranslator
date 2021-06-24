from MorseCodeDict import MORSE_CODE_DICT
from Translator import SplitBy, Translator


morse_code_translator = Translator(MORSE_CODE_DICT, SplitBy.LETTERS, space_per_letter=3, space_per_word=7)

print("************** Morse Code Translator *****************")

while True:

    input_message = input("Please type a message to translate to Morse Code: ")

    translated_message = morse_code_translator.translate(input_message)

    print(translated_message)

    is_quiting = input("Press 1 and then return to quit")

    if is_quiting == 1:
        break

