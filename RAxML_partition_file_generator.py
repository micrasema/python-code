import sys #module needed to open outside file
InFile = sys.argv[1] #assigns this variable to file opened, specified in shell
OutFileName = str('1kite_1478g_146t_nt_partition') #this refers to a BLANK file that you 
                                                   #MUST have already created (choose any name)


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
