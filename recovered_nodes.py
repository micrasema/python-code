#This code should take a file with the universal list of genes and compare it to a subset of genes
#then write whether the gene in the subset with a 1 next to it and write the genes not in the subset
#with a 0 next to them.


#Programming outline: take the universal code line by line and assign each value to a variable
#determine if it matches with any line within the subset by looping it through a set
#if there is a match, then write it to the outfile. In cases that there is no match, write the gene name
#to the outfile with a 0 next to it. This can be done if a count is reached. If the count = 1, then write
#the gene'\t'1, if the count is set at 0, then write gene'\t'0. This should give a sortable output, with
#all genes included and those that match up with a 1 next to them.

import sys  

file1 = sys.argv[1] #use two files, you can call them as:
                  #python2.7 recovered_nodes.py <filename1> <filename2>
                  #designates the first file as file1
                  #the first file should be the universal file, the second should be
                  #the subset file from each node

file2 = sys.argv[2] #designates the second file as file2

name = str(file2)

f1 = open(file1, 'r') #opens files for reading
f2 = open(file2, 'r')
o1 = open((name + '1.txt'), 'w')

f2s = {line.strip('\n') for line in f2} #assigns the data in file2 to a "set"

for line in f1: #iterates through file one (all genes)
    line = line.strip('\n') #removes end of line characters from gene name
    count = 0
    if line in f2s: #checks if the each gene is contained within the subset from the f2s "set"
        count += 1 #if it is, adds a 1
        print (str(line) + '\t' + str(1)) #prints to screen just so the program looks like it is doing something
        o1.write(str(line) + '\t' + str(1) + '\n') #writes to outfile with an end of line characeter
    if count == 0: #checks if the character is NOT in the set
        print (str(line) + '\t' + str(0)) #prints to terminal
        o1.write(str(line) + '\t' + str(0) + '\n') #writes output to outfile

f1.close()
f2.close()
o1.close() #close all files then the program ends.
            