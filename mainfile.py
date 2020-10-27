#q5

import re 

#defining hapax with one argument which contains the filename
# find.all() will iterate over all the lines of the file and return it without overlapping
#lower() to make sure not case sensitive 
#frequencies // to make sure that the word only occurs once 

def hapax_legomenon(filename):
    file = open(filename)
    words = re.findall('w+',file.read().lower())
     check_frequent = {key: 0 for key in words}
    for word in words:
        check_frequent[word] += 1
    for word in check_frequent:
        if check_frequent[word] == 1:
            print(word)

hapax(book_file)


    
