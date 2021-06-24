from enum import Enum

SINGLE_SPACE_STR = " "


def capitalize_keys(d):
    """
    Returns a new dictionary with uppercase string values for the keys by looping through the key and values
    of the dictionary passed in the function argument.  The values are copied into the new dictionary.
    """
    result = {}
    for key, value in d.items():
        try:
            upper_key = key.upper()
            result[upper_key] = value
        except TypeError:
            print(f"The keys are not all str types from the dictionary passed in the capitalize_keys function argument."
                  f"Can only call the upper method on str")
    return result


class SplitBy(Enum):
    """To use with Translator class as an argument for split_type"""
    LETTERS = 0
    WORDS = 1


class Translator:
    """
    A class to translate a string value using a dictionary
    ...

    Attributes
    ----------
    translator_dict : dict
        A dictionary with the keys as str types and the values as str type.
        A new dictionary is created where the keys are all uppercase.
    split_type : 'SplitBy'
        The splitby attribute indicates to the class to lookup a single letter at a time or a whole word
    space_per_letter : int
        The str space added to the translation after each letter.  Default is 0.  Only used if splitby is by letters
    space_per_word : int
        The str space added to the translation after each word.
        It is used when there is a space in the sentence to translate

    Methods
    -------
    translate(sentence: str) -> str
        Returns the translation as a string of the string sentence passed as a argument in the method
    """

    def __init__(self , translator_dict: dict,
                 split_type: 'SplitBy',
                 space_per_letter: int = 0,
                 space_per_word: int = 1) -> None:
        """
        Parameters
        ----------
        translator_dict : dict
            A dictionary with the keys as str types and the values as str type.
            A new dictionary is created where the keys are all uppercase.
         split_type : 'SplitBy'
            The splitby attribute indicates to the class to lookup a single letter at a time or a whole word
        space_per_letter : int
            The str space added to the translation after each letter.  Default is 0.  Only used if splitby is by letters
        space_per_word : int
            The str space added to the translation after each word.
            It is used when there is a space in the sentence to translate
        """
        self.translator_dict = capitalize_keys(translator_dict)
        self.split_type = split_type
        self.space_per_letter = space_per_letter
        self.space_per_word = space_per_word

    def __repr__(self):
        return f"{self.__class__.__name__}(self.translator_dict, " \
               f"self.split_type={self.split_type}," \
               f"self.space_per_letter={self.space_per_letter}," \
               f"self.space_per_word={self.space_per_word}"

    def translate(self, sentence: str) -> str:
        """
        translates the sentence param using the class instance
        translator_dict
        returns the translation as a string
        """
        if sentence == '':
            return sentence
        split_sentence = self._split_sentence(sentence, self.split_type)
        translation = self._loop_through_translation_dict_using(split_sentence)
        return translation

    def _loop_through_translation_dict_using(self , before_translation: list[str]) -> str:
        """
        Creates an empty list named translation_list
        Loops through each index in the before_translation list
        Adds the translated index to the translation_list using the instances translator_dict
        returns the translation_list as a string.
        """
        translation_list = []
        for string_data in before_translation:
            if string_data != " ":
                translation = self.translator_dict.get(string_data.upper(), "")
                if translation:
                    translation_list.append(translation)
                    if self.space_per_letter:
                        translation_list.append(SINGLE_SPACE_STR * self.space_per_letter)
            else:
                translation_list.append(SINGLE_SPACE_STR * self.space_per_word)
        translation_string = "".join(string for string in translation_list)
        return translation_string

    def _split_sentence(self, sentence: str, split_type: 'SplitBy') -> list[str]:
        """
        Splits the sentence string param into a list by characters or words
        instructed by the param split_type.

        Returns the result into a List with str types
        """
        if split_type == SplitBy.LETTERS:
            # add split flag in the empty strings
            return [char for char in sentence]
        elif split_type == SplitBy.WORDS:
            return sentence.split()
        else:
            raise TypeError("incorrect split_type used.  "
                            "Please use SplitByEnum correctly.  "
                            "0 for Letters and 1 for words")


