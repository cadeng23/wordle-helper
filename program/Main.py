#Caden Gustafson
old = []
def read_words(words):
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
    #Step 1: store the known letters and spots for the letters 
    known = [] #the known letter(s) in the word
    spotKnown = [] #The know indexes that correspond to the word in the same spot on the known list
    for x in current:
        if x != '_':
            if x.islower() == False:
                low = x.lower()
            else:
                low = x
            i = current.index(x)
            known.append(low)
            spotKnown.append(i)
    #End Step 1
    #Step 2: filter through all the words for the letters in the spots that are known
    temp = []
    possible = []
    print(known)
    print(spotKnown)
    for word in words:
        spot = spotKnown[0]
        if known[spot] == word[spotKnown[0]]:
            possible.append(word)
    print(possible)
    for here in spotKnown:
        temp = possible
        possible = []
        for word in words:
            spot = spotKnown.index(here)
            if known[spot] == word[here] and word in temp:
                possible.append(word)
    #End Step 2
    #Step 3: filter out based on the letters that are known not to be in the word
    print('after step 2 =',possible)
    temp = possible
    possible = []
    c = 0
    for x in temp:
        for a in outed:
            if a not in x:
                c += 1
            else: 
                break
        if c == len(outed):
            possible.append(x)
        c = 0
    #End Step 3
    #Step 4: check to see what letters are known but do not have a spot yet
    temp = possible
    print('after step 3 =',possible)
    final = []
    p = 0
    print(len(inned))
    if len(inned) > 0:
        for x in temp:
            for i in inned:
                if i in x:
                    p += 1
                else:
                    break
            if p == len(inned):
                final.append(x)
            p = 0
    if len(inned) == 0:
        final = temp
    #End Step 4
    t = 1
    print(final)
    for f in final:
        print('answer', t, '=', f)

def main():
    words = []
    words = read_words(words)
    #print(words)
    outed, inned, current = input_one(words)
    filtered (words, outed, inned, current)

main()
