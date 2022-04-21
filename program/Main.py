#Caden Gustafson
old = []
words = []
def read_words():
    file = open("./program/words.txt",'r')
    old = file.readlines()
    for line in old:
        new = line[:-2]
        words.append(new)
    print(words)


def main():
    read_words()

main()
