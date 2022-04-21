#Caden Gustafson
old = []
words = []
possible = []
first = []
second = []
third = []
fourth = []
filters = [first, second, third, fourth]
def read_words():
    file = open("./program/newWords.txt",'r')
    old = file.readlines()
    for line in old:
        new = line[:-1]
        words.append(new)
    #print(words)
    return words

def input_one(words):
    outed = []
    inned = []
    current = input('Please enter the word you have so far(use _ for the parts you do not have yet):')
    out = input('What letters do you know are not in the word?:')
    inside = input('what letters are in the word but you dont know the spot for?:')
    for spot in out:
        if spot != ' ':
            if spot.islower() == False:
                letter = spot.lower()
            else:
                letter = spot
            outed.append(letter)
        else:
            continue
    for spot in inside:
        if spot != ' ':
            if spot.islower() == False:
                letter = spot.lower()
            else:
                letter = spot
            inned.append(letter)
        else:
            continue
    print(outed)
    print(inned)
    print(current)
    return outed, inned, current

def filtered(words, outed, inned, current):
    known = []
    spotKnown = []
    for x in current:
        if x != '_':
            if x.islower() == False:
                low = x.lower()
            else:
                low = x
            i = current.index(low)
            known.append(i)
            spotKnown.append(low)
    s = 0
    while(True):
        for word in words:
            if word[]

def main():
    read_words()
    input_one(words)

main()
