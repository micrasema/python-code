import sys

file1 = sys.argv[1]

outname = (str(file1) + 'out')

inFile = open(file1, 'rb')

outFile = open(outname, 'wb')

line_number = 0

for line in inFile.readlines():
    new_line_list = line.split(' ')
    outFile.write(new_line_list[0] + '\t' + new_line_list[4] + '\n')
    line_number += 1

    
        
inFile.close()
outFile.close()