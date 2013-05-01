import pylab


WORDLIST_FILENAME = "rates.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip())
    print "  ", len(wordList), "words loaded."
    return wordList
    print wordList
    
def makeHistPlot(wordList, numBins=10):
    """
    creates a histogram
    for rates of everything
    """
    list = []
    for i in wordList:
        list.append(float(i))
    pylab.hist(list, numBins, color = 'g')
    pylab.title('Evolutionary rates from COI gene, split into ' + str(numBins) + ' bins!')
    pylab.xlabel("Consistency Index of individual characters from cytochrome oxidase subunit I")
    pylab.ylabel('Frequency')
    pylab.show()
    
if __name__ == '__main__':
    wordList = loadWords()
    makeHistPlot(wordList)