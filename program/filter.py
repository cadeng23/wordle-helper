all_words = []
five_let = []

def read_allwords():
    all = open("./program/words.txt",'r')
    all_words = all.readlines()
    new_all_words = []
    for line in all_words:
        new = line #[:-2]
        if len(new) == 6:
            five_let.append(new)
        else: 
            continue
    print(five_let)
    all.close()
    return five_let

def write_file():
    writing = open("./program/newWords.txt",'w')
    for line in five_let:
        writing.write(line)
    writing.close()

read_allwords()
write_file()