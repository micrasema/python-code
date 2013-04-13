import sys  

file1 = sys.argv[1] #use two files, you can call them as:
                  #python3 combine_data_sheets_zip.py <filename1> <filename2>

file2 = sys.argv[2]

o = open('output.txt', 'wb')

fh = open(file1, 'rb')
fh2 = open(file2, 'rb')

for line in fh.readlines():
    o.write(line.strip('\r\n') + '\t' + fh2.readline().strip('\r\n') + '\n')

## If you want to write remaining files from input2.txt:
# for line in fh2.readline():
#     o.write(line.rstrip('\r\n') + '\n')

fh.close()
fh2.close()
o.close()