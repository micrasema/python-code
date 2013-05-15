import sys

inFile = open(sys.argv[1], 'r')

line_number = 1
for line in inFile:
	if line_number == 66:
		string_of_rates = line
	line_number += 1

list_of_rates = string_of_rates.split(" ")

count = 0
for i in range(658):
	print list_of_rates[count]
	count += 1




