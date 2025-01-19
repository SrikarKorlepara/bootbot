	
def printWords(pathOfFile):
	with open(pathOfFile) as f:
		file_contents=f.read()
		return file_contents

def countOfWords(text):
	words=text.split()
	return len(words)

def count_characters(text):
   
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def makeReport(hm):
	for char in hm:
		print(" The \'"+char+"\' character was found "+str(hm[char])+" times")


bookText = printWords("books/frankenstein.txt")
wordCount = countOfWords(bookText)
countCharacters= count_characters(bookText)
makeReport(countCharacters)




















