#need commentary later 
def avg_wordlen(filename): 
    length = []
    file = open(filename, 'r', encoding = 'utf-8')
    for words in file.read().split():
        length.append(len(words))

    for a in length:
        average = sum(length)/len(length)
    return average

print(avg_wordlen(book_file))
