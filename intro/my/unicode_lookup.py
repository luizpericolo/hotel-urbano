import sys
import unicodedata

def search(word):
    """
        Searches for a character that has word in its name
        :param word:string
        :return: tuple list (character, character name)

        # Find with last word
        >>> ('♥', "BLACK HEART SUIT") in search("SUIT")
        True

        # Find with middle word
        >>> ('♠', "BLACK SPADE SUIT") in search("SPADE")
        True

        # Find with first word
        >>> ('♣', "BLACK CLUB SUIT") in search("BLACK")
        True
    """

    found = []
    for i in range(20, sys.maxunicode):
        char = chr(i)
        try:
            char_name = unicodedata.name(char)
        except ValueError:
            continue

        if word.upper() in char_name:
            found.append((char, char_name))

    return found

if __name__ == "__main__":
    _, word = sys.argv
    print(search(word))
