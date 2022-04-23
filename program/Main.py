#Caden Gustafson
old = []
words = []
possible = []
temp = []
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

def filtered(words, outed, inned, current, possible):
    known = [] #the known letter(s) in the word
    spotKnown = [] #The know indexes that correspond to the word in the same spot on the known list
    for x in current:
        if x != '_':
            if x.islower() == False:
                low = x.lower()
            else:
                low = x
            i = current.index(x)
            known.append(x)
            spotKnown.append(i)
    s = 0
    for word in words:
        if word[spotKnown[s]] == known[s]:
            possible.append(word)
    s += 1
    if len(spotKnown) > 1:
        temp = possible
        possible = []
        for word in temp:
            if word[spotKnown[s]] == known[s]:
                possible.append(word)
    s += 1
    if len(spotKnown) > 2:
        temp = possible
        possible = []
        for word in temp:
            if word[spotKnown[s]] == known[s]:
                possible.append(word)
    s += 1
    if len(spotKnown) > 3:
        temp = possible
        possible = []
        for word in temp:
            if word[spotKnown[s]] == known[s]:
                possible.append(word)
    print(possible)

def main():
    read_words()
    outed, inned, current = input_one(words)
    filtered (words, outed, inned, current, possible)

main()
