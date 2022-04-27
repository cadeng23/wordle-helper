#Caden Gustafson
old = []
def read_words(words):
    file = open("./program/PickedWords.txt",'r')
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
    print('letters known =', known)
    print('spot known =', spotKnown)
    #End Step 1
    #Step 2: filter through all the words for the letters in the spots that are known
    temp = []
    possible = []
    print(spotKnown)
    print(known)
    print('size after step 1 =', len(words))
    if len(spotKnown) > 0:
        for word in words:
            spot = spotKnown[0]
            if known[0] == word[spot]:
                possible.append(word)
                #print('known =',known[spot], 'at spot ', spot)
                #print('spot =', word[spotKnown[0]], 'at spot ', spotKnown[0])
        print('possible size =', len(possible))
        for here in spotKnown:
            temp = possible
            possible = []
            for word in words:
                spot = spotKnown.index(here)
                if known[spot] == word[here] and word in temp:
                    possible.append(word)
    if len(spotKnown) == 0:
        for word in words:
            possible.append(word)
    #End Step 2
    #Step 3: filter out based on the letters that are known not to be in the word
    print('left after step 2 =', len(possible))
    print('size of outed =', len(outed))
    if len(outed) > 0:
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
    print('size after step 3 =',len(possible))
    print('inned size =', len(inned))
    if len(inned) > 0:
        temp = possible
        possible = []
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
                    possible.append(x)
                p = 0
        if len(inned) == 0:
            possible = temp
    #End Step 4
    #Step 5: ask for the positions that the inned list cannot be in
    r = len(inned)
    curr = 0
    while(True):
        arr = []
        if curr < len(inned):
            b = input('how many spots do you know that ', inned[curr], 'is not in the word?')
            b = int(b)
            for a in range(b):
                spot = input('spot that ', inned[curr].upper(), ' is not in?')
                spot = int(spot)
                arr.append(spot)
            for word in possible:
                for z in spot:
                    p = 0
                    if inned[curr] != word[z]:



                


            
    #End Step 5
    temp = possible
    possible = []
    for g in temp:
        if g not in possible:
            possible.append(g)
    t = 1
    for f in possible:
        print('answer', t, '=', f)
        t += 1

def main():
    words = []
    words = read_words(words)
    outed, inned, current = input_one(words)
    filtered (words, outed, inned, current)

main()
