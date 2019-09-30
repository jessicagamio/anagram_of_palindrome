"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # Check to see if this is NOT a anogram first
    
    if len(word) == 1:
        print('================> this is ',True)
        return True


    elif word == word[::-1]:
        return False

    else:
        word_length = len(word)
        letter_dict = {letter:word.count(letter) for letter in set(word)}
        num_of_letter_set = set(letter_dict.values())

        # for even number words check to see if letter has pairs
        if word_length % 2 == 0:
            for number in num_of_letter_set:
                if letter % 2 == 0:
                    return True
                else:
                    return False



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
