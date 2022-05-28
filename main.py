# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    f = open(filename+".txt", "r")
  
    readfile=f.read()
    print(readfile)
    return readfile


def count_words():
    text = read_file_content("C:\\Users\\Reading-Text-Files\\story")
    # [assignment] Add your code here
    count1 = text.count(" as ")
    count2=text.count(" would ")

    return {"as": count1, "would": count2}

#read_file_content("C:\\Users\\Reading-Text-Files\\story")
print(count_words())