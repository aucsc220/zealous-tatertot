"""
demo_functions.py

Anna Koop, Sept 2015

This contains a random assortment of functions, mostly existing to illustrate
the use of the doctest module and assorted other things.
"""

import string
from collections import defaultdict

def cleanup_word(word):
    """
    Return a string that contains all the letters, in the correct order,
    lowercase, with no special characters except inner spaces.
    
    >>> cleanup_word('2015')
    ''
    >>> cleanup_word("HELLO FRIENDS!")
    'hello friends'
    >>> cleanup_word("Party like it's 1979!")
    'party like its'
    >>> cleanup_word("  hello...")
    'hello'
    """
    ##Updated Sept 22 2:59 PM by Zoe Tomkow
    ##We are deleting spaces before and after the sentance.
    ##We are also adding spaces between words.
    letters = []
    word.split(' ')  ##Split our word up for easier handling.  Extra code, but 
    for eachWord in word:  ##easier to read.
        for eachLetter in eachWord :
            if eachLetter in string.ascii_letters :  ##is it ascii letter?
                letters.append(eachLetter.lower())   ##add it to the list and lower case
            elif eachLetter == ' ' and letters !=[] :  ##this adds a space if it's a space ONLY if 
                letters.append(' ')                    ##the list is not empty.  This handles spaces before a sentance.
    if letters != [] :     
        if letters [-1] == ' ' :    ##this removes an extra space at the end if there is one.
            del letters[-1]
    return ''.join(letters)

def is_palindrome(word):
    """
    Returns true of the word is a palindrome, false otherwise
    
    >>> is_palindrome('tot')
    True
    >>> is_palindrome('mot')
    False
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('Aibohphobia')
    True
    >>> is_palindrome('Amore, Roma')
    True
    >>> is_palindrome('Name no one man.')
    True
    >>> is_palindrome('')
    True
    >>> is_palindrome('x')
    True
    """
    midpoint = len(word)//2
    
    # check the first half of the letters against the back half
    for i, v in enumerate(word[:midpoint]):
        if v != word[-i]:
            return False
    return True

def has_doubles(word):
    """
    Returns true if the word has duplicate letters, false otherwise
    
    >>> has_doubles('wow')
    True
    >>> has_doubles('tater')
    True
    >>> has_doubles('OMnom')
    True
    >>> has_doubles('doubles')
    False
    >>> has_doubles('Can haz taters?')
    True
    """
    singles = set(word)
    if len(singles) < len(word):
        return True
    else:
        return False
    
def can_spell(word, allowed_letters):
    """
    Return true if the word can be spelled using the letters in allowed_letters
    
    >>> can_spell('wow', ['w', 'o'])
    False
    >>> can_spell('wow', ['w', 'w', 'o'])
    True
    >>> can_spell('wow', ['a', 'b', 'c', 'w', 'o', 'w'])
    True
    >>> can_spell('Tot', ['t', 'o', 't'])
    True
    >>> can_spell('Aibohphobia', string.ascii_letters*4)
    True
    """
    wordLength = len(word)
    myList = list(allowed_letters)
    location = 0
    for w in word:
        if w.isupper(): # replaces an uppercase letter
            myList.insert(location,w.lower())
        elif w not in myList:
            return False
        else:
            myList.remove(w) #pop a letter from a copy allowed_letters's list if found
        location +=1   
    return True
def display_masked_word(word, found_letters=None):
    """
    Print the word to the screen with all the letters that do not occur in found_letters
    blanked out with an underscore. See doctests for required spacing.
    
    >>> display_masked_word('hello', ['e'])
    _ e _ _ _
    >>> display_masked_word('cheezeburger', ['a', 'b', 'c', 'd', 'e'])
    c _ ee _ eb _ _ _ e _
    >>> display_masked_word('Frosted flakes', ['f'])
    f _ _ _ _ _ _  f _ _ _ _ _
    >>> display_masked_word('tatertots and ketchup', ['a', 't', 'e'])
    tate _ t _ t _  a _ _   _ et _ _ _ _
    >>> display_masked_word('cheezeburger')
    _ _ _ _ _ _ _ _ _ _ _ _
    """
    if not found_letters:
        found_letters = []
    
    display = ['_']*len(word)
    for i, v in enumerate(word):
        if v in found_letters:
            display[i] = v
    print(' '.join(display))
    
def sort_by_length(words):
    """
    Take a list of words and return a list of word lists, grouped by word-length from
    smallest to largest with the words in the list sorted alphabetically
    
    >>> sort_by_length(['a', 'cat', 'friend'])
    [['a'], ['cat'], ['friend']]
    >>> sort_by_length(['tater', 'tatertots', 'a', 'meal', 'of', 'champion', 'cats'])
    [['a'], ['of'], ['cats', 'meal'], ['tater'], ['champion'], ['tatertots']]
    """

    word_dict = defaultdict(list)
    
    for w in words:
        word_dict[len(w)].append(w)

    word_lists = []
    for k in sorted(word_dict):
        word_lists.append(word_dict[k])

    for k in word_dict:
        word_dict[k].sort()
        
    return word_lists

def pretty_print_words(words):
    """
    Take a list of words and print them in columns by length, alphabetized.
    
    >>> pretty_print_words(['a', 'cat', 'friend'])
    a  cat  friend
    >>> pretty_print_words(['tater', 'tatertots', 'a', 'meal', 'of', 'champion', 'cats', 'om', 'nom'])
    a  of  nom  cats  tater  champion  tatertots
       om       meal
    """
    word_lists = sort_by_length(words)
    lengths = [len(w) for w in word_lists]

    for row in range(max(lengths)):
        row_words = []
        for l in word_lists:
            row_words.append(l[row])
        print("  ".join(row_words))
        

if __name__ == "__main__":
    print("Starting doctests...")
    import doctest
    doctest.testmod()
    print("Done doctests!")

    

