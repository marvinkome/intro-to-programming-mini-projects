import re

def proof_read_text():
    file = open("C:\\Users\\yyy\\Documents\\txt\\top.txt")
    content = file.read()
    #print(content)
    check_profanity(content)
    file.close()

def check_profanity(words):
    curse_words = ['shit', 'fuck', 'ass', 'nigga']
    words = words.split(' ')
    curse_words_found = []
    for word in words:
        word = re.sub('[-.]', '', word)

        if word in curse_words:
            curse_words_found.append(word)

    no_curse_words = len(curse_words_found)

    if no_curse_words != 0:
        for curse_word in curse_words_found:
            print("Curse words found: " + curse_word)

        return False

    print('No curse word found')
    return True

proof_read_text()
