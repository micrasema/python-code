#this script trims taxa from phylip files that you wish not to include in analyses
#it is only compatible with python3. Requres a separate text file with the taxa you wish to
#keep in your file listed on separate lines

import sys  

file1 = sys.argv[1] #use two files, you can call them as:
                  #python3 keep_subset_taxa.py <filename1> <filename2>
                  #designates the first file as file1
                  #the first file should be the file you wish to trim the second should be
                  #the subset file with the names you wish to include

file2 = sys.argv[2] #designates the second file as file2

name = str(file1)
numbertax = 0
numberchar = 0
LineNumber = 0
f1 = open(file1, 'r') #opens files for reading
f2 = open(file2, 'r')
o1 = open((name + '.phy'), 'a') #creates a new file for writing and adds ".phy" extension 
                                #make easy designation of which file is the trimmed one

f2s = {line.strip('\n') for line in f2} #creates a set including the taxa you wish to include

numbertax = 0  #sets counters for various variables to be used below
numberchar = 0
LineNumber = 0

for line in f1:        #this block saves the number of characters in the file
    if LineNumber == 0:
        chardata = line.split(' ')
        numberchar += int(chardata[1])
        LineNumber += 1
    elif LineNumber > 0:             #this block saves the number of new taxa
        taxon_name = line.split(' ')
        print(taxon_name[0])
        if taxon_name[0] in f2s:
            numbertax += 1
        LineNumber += 1
taxa_char = str(numbertax) + ' ' + str(numberchar)
print(taxa_char)
o1.write(taxa_char + '\n')

f1.close()
f2.close()
o1.close()

f1 = open(file1, 'r')
f2 = open(file2, 'r')
o1 = open((name + '.phy'), 'a')

f2s = {line.strip('\n') for line in f2}

LineNumber = 0   #this block determines which taxa to trim (really it determines which taxa
for line in f1:  #to include, thus excluding unwanted taxa, it retrieves this information
    if LineNumber == 0: #from your text file that includes taxa you want to keep
        LineNumber += 1
    if LineNumber > 0:
        taxon_name = line.split(' ')
        if taxon_name[0] in f2s:
            print(line)
            o1.write(line)

f1.close()
f2.close()
o1.close()