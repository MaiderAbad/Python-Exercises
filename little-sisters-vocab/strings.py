def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    prefix='un'
    pre_res = prefix + word
    return pre_res


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix= vocab_words[0]
    pre_res = [prefix + sub for sub in vocab_words[1:]]
    finallist= [prefix]+pre_res
    separator = ' :: '
    return separator.join(finallist)


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    suffix='ness'
    rms=word.replace(suffix, '')
    if rms[len(rms)-1]=='i':
        rms=list(rms)
        rms[len(rms)-1]='y'
        rms="".join(rms)
    return rms


def noun_to_verb(sentence, index):
    """ 

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    if sentence[len(sentence)-1]=='.':
        spls0=sentence.split('.')[0]
        spls=spls0.split()
    else:
        spls=sentence.split()
    suffix='en'
    suf_res = spls[index]+ suffix
    return  suf_res

print (add_prefix_un("happy"))
print (make_word_groups(['en', 'close', 'joy', 'lighten']))
print (remove_suffix_ness("heaviness"))
print (noun_to_verb('The black oil got on the white dog.', 1 ))

