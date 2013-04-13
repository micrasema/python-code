from glob import glob
import sys # the sys module is necessary to allow us to use sys.argv


InFileName = sys.argv[1] # this allows us to open a filename indicated by our terminal script
                         #use the syntax "python final_script_remove_taxa.py filename" to work the script

InFile = open(InFileName, 'r') #opens a pipeline to the file to be read line by line

OutFileName = str(InFileName) + '.phy' # appends the .phy to the end of the phylip file

OutFile = open(OutFileName, 'w') #writes the number of taxa and characters to top of file

#This portion of the script counts the number of taxa that meet the requirement of over
#150 nucleotides and rewrites the number of taxa block at the beginning of the file

numbertax = 0
numberchar = 0
LineNumber = 0
for Line in InFile:
    if LineNumber == 0: #takes the data from the taxa and character line
        chardata = Line.split(' ') #splits values of taxa and character separated by a space
        numberchar += int(chardata[1]) #adds character data
        LineNumber += 1  #adds line
    elif LineNumber > 0:
        count = 0 #starts the count for the number of nucleotides in the
        for i in Line:
            if i == 'A' or i == 'C' or i == 'G' or i == 'T': #checks for
                count += 1
            
        if count > 150:
            Line = Line.strip('\n')
            numbertax += 1 #keeps track of how many taxa you know have in your script
        LineNumber += 1 #keeps line count
           

taxa_char = str(numbertax) + ' ' + str(numberchar) #variable holding both taxon info and character info
print taxa_char #gives value of taxa and character to screen
OutFile.write(taxa_char+'\r') #writes value to file plus carriage return

InFile.close() #must close the file before re-opening it
OutFile.close() #must close the writing process

InFileName = sys.argv[1] #reassigns filename, same as used above

InFile = open(InFileName, 'r') #reopens file indicated earlier

OutFile = open(OutFileName, 'a') #opens existing file for appending 'a', file already has first line

LineNumber = 0
for Line in InFile:
    if LineNumber > 0:
        count = 0 #starts the count for the number of nucleotides in the line
        for i in Line:
            if i == 'A' or i == 'C' or i == 'G' or i == 'T': #checks for the number of nucleotides for a certain taxon
                count += 1
                
        if count > 150:
            Line = Line.strip('\n')
    
            print str(Line) #prints the line that has met the expectation of having information for over 150 nucleotides
            OutFile.write(str(Line)+'\r') #writes the new phylip file line by line
    LineNumber += 1
    
InFile.close()
OutFile.close()
