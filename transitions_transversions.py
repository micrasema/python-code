#this code retrieves important phylogenetic statistics form a RAxML.info file
#and outputs them to a tab delimited text file
from glob import glob
import sys # the sys module is necessary to allow us to use sys.argv


InFileName = sys.argv[1] # this allows us to open a filename indicated by our terminal script
                         #use the syntax "python transitions_transversions <filename>" to work the script
                         
InFile = open(InFileName, 'r') #opens a pipeline to the file to be read line by line

OutFileName = "transitions_transversions.txt"  # assigns a name to the outfile, you can adjust outfile
                                           #name by changing the string within the quotes

OutFile = open(OutFileName, 'a') #writes the file and puts it into "append" mode

for Line in InFile:
    Line = Line.strip()
    if Line.startswith("alpha"):
        print Line
        OutFile.write(str(InFileName)+'\t'+str(Line))
    if Line.startswith("rate") or Line.startswith("freq"):
        print Line
        OutFile.write('\t'+str(Line))
    if Line.startswith("Drawing"):
        OutFile.write('\r''\n')

InFile.close()
OutFile.close()
