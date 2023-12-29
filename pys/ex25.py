
# A break_words függvény defje, ami külön szedi azokat a mondat részeket, amik
#között szóköz van, azaz a szavakat egy words nevű listába rakja
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words



#A sort_words függvény defje, ez az előző words nevű listában lévő szavakat
#ABC sorrendbe rakja
def sort_words(words):
    """Sorts the words"""
    return sorted(words)



#A print_first_word nevű függvény megfogja az első szót a listában amit
#bemenetre kap és kiszedi a listából és egy word nevű változóba rakja


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


#A print_last_word nevű függvény megfogja az utolsó szót a listában amit
#bemenetre kap és kiszedi a listából és egy word nevű változóba rakja

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)



#Nincs különbséget a sort_words és a sort_sentence között, de fentebb kivettük
#az első és az utolsó szót a sort_words-ből és később újra kell a teljes lista
#megint

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and the last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
