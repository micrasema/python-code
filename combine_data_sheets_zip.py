#for use with python3, doesn't work with python2.7
import sys  

file1 = sys.argv[1] #use two files, you can call them as:
                  #python3 combine_data_sheets_zip.py <filename1> <filename2>

file2 = sys.argv[2]

with open(file1) as f1,open(file2) as f2,open("combined_data.txt","w") as fout:
     for t in zip(f1,f2):
         fout.write('\t'.join(x.strip() for x in t)+'\n') #using zip adds lines