# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    f = open(filename,"r")
    word = f.read()
    f.close()
    return word


def count_words():
    text = read_file_content("./story.txt")
    # # [assignment] Add your code here
    words = text.split()
    words = filter(str.isalnum, words)
    fWords = [a for a in words]
    d = {x:fWords.count(x) for x in fWords}

    return d


s = read_file_content("./story.txt")
# print(s)
print(count_words())