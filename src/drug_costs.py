#!/usr/bin/env python

"""pharmacy_counting.py: Reads in dataset of pharmaceutical information and prints output file summarizing prescriber and total cost information for each drug."""

__author__ = "Lauren Kahre"
__credits__ = ["Lauren Kahre"]
__version__ = "1.0.1"
__maintainer__ = "Lauren Kahre"
__email__ = "lekahre@gmail.com"

import sys
import argparse
import csv
import math

#Argument parser, shows help text for input variables.
if len(sys.argv) < 2:
	print('Too few arguments, please specify input and output filenames.')
parser = argparse.ArgumentParser(description='Reads, sorts, and summarize prescriber and total cost data for different pharmaceuticals.')
parser.add_argument('Infile', metavar='infile', type=str, nargs='+',
                   help='The input dataset filename, including directory location')
parser.add_argument('Outfile', metavar='outfile', type=str, nargs='+',
                   help='The output filename for summarized data, including directory location')

args = parser.parse_args()

infile = sys.argv[1]		#Input file name
outfile = sys.argv[2]		#Output file name

#Read dataset into multidimensional list, verify file format and dataset size
datafile = open(infile, 'r')
readdata = csv.reader(datafile, delimiter=',')
next(readdata)             	#skips header line
data = []
entrycount = 0
printrate = 1000000.			#Progress statement print gap for large files

for entry in readdata:
	data.append(entry)
	if len(data[entrycount]) != 5:
		print('Incorrect file or file format. Number of columns is not correct. File should contain: prescriber id, prescriber last name, prescriber first name, drug name, drug cost.')
		quit()
	entrycount = entrycount + 1
	if math.ceil(entrycount/printrate) == entrycount/printrate:		#Print progress statement for large datasets
		print('Entry ' + str(entrycount) + ' read.')
print('File read complete. ' + str(entrycount) + ' total entries in dataset.')

#data format: [prescriber id, prescriber last name, prescriber first name, drug name, drug cost]

#Find number of unique prescribers for each drug and total cost
drug_data = {} 		#cost summation and unique prescriber dictionary for drugs- contains a list in the format unique_prescriber_list, unique_prescriber_num, total_cost

for i in range(len(data)):
	presc_id = int(data[i][0])											#Convert prescriber id to integer for easier comparison and data validation
	drug_name = data[i][3].upper()      								#Make drug name case-insensitive in case not all are fully capitalized
	drug_cost = float(data[i][4])										#Convert drug cost to float for summation and data validation
	if drug_name in drug_data:											#If drug already exists in dictionary, perform summation and check for unique prescriber
		if presc_id in drug_data[drug_name][0]:								#If prescriber already found, leave list as is	
			pass
		else:																#If prescriber is new, add to list
			drug_data[drug_name][0].append(presc_id)
			drug_data[drug_name][1] = len(drug_data[drug_name][0])				#Sets current number of unique prescribers
			drug_data[drug_name][2] = drug_data[drug_name][2] + drug_cost		#Sums total drug cost
	else:																#If drug does not exist in dictionary, create new entry with drug information
		drug_data[drug_name] = [[presc_id], 1, drug_cost]
	if math.ceil((i+1)/printrate) == (i+1)/printrate:								#Print progress statement for large datasets
		print('Entry ' + str(i+1) + ' of ' + str(len(data)) + ' complete.')
print('Drug costs and prescribers summed.')

#Put dictionary in list for sorting
sum_data = []

for key, value in drug_data.items():
    drug_entry = [key, value[1], value[2]]
    sum_data.append(drug_entry)

#Sort list by total cost, then name, in reverse order
sum_data.sort(key=lambda x: (x[2], x[0]), reverse=True)
print('Drug data sorted. There are ' + str(len(sum_data)) + ' unique drugs.')

#Output file results
file = open(outfile, 'w+')
headerstring = 'drug_name,num_prescriber,total_cost\n'
file.write(headerstring)
drugcount = 0;

for drug in sum_data:
	datastring = drug[0] + ',' + str(drug[1]) + ',' + str(drug[2]) + '\n'
	file.write(datastring)
	drugcount = drugcount + 1
	if math.ceil(drugcount/printrate) == drugcount/printrate:				#Print progress statement for large datasets
		print('Entry' + str(drugcount) + ' of ' + str(len(sum_data)) + ' saved to file.')
print('File write complete.')
	
file.close()

			
		
