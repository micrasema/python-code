#this file takes a file and assigns
import sys 
InFile = sys.argv[1] #assigns this variable to file opened, specified in shell
OutFileName = str(InFile) + '_partition' #this refers to a BLANK file that you 
                                                  


OutFile =open(OutFileName, 'a') #this opens up the file for 'appending' to add new lines of charsets

with open(InFile) as f: #opens the file specified in the shell, can do multiple with shell loop
    lis=[x.split() for x in f] 

for x in zip(*lis):
    full_line = []
    for y in x:
        full_line.append(y)
    print str('DNA, ') + str(InFile) + str('= ') + str(', '.join(full_line)) + ('\r')
    OutFile.write(str('DNA, ') + str(InFile) + str(' = ') + str(', '.join(full_line)) + ('\r'))
#print('\n')
