# Table of Contents
1) Program Function
2) Usage
3) Prerequisites
4) Basic Approach
5) Error Checking


# Program function:
This program takes the cleaned and simplified dataset of prescription information from the Centers for Medicare & Medicaid Services
and compiles it to summarize the total cost and number of unique prescribers for each individual drug. 

# Usage:
drug_costs.py input_file output_file

# Prerequisites:
The Python 3 standard library, including csv and argparse.

# Basic Approach:
This program requires a comma-delimited input file with the columns id, prescriber_last_name, prescriber_first_name, drug_name, and 
drug_cost, in that order, and assumes the first row of the file is a header line. 

After reading the dataset into a multidimensional list, it loops through each record, creating a dictionary with unique drug names
as keys. The value for each key is a list. The first index of that list is a list of unique prescriber ids for that drug, the second 
is an integer length of that list, and the third is a float total cost of all prescriptions for that drug. Because it is possible for 
multiple doctors to have the same name, unique prescribers are determined via id number, not name. Once all records have been 
examined, the dictionary is transferred to a new multidimensional list for sorting by total cost and drug name in descending order, 
then printed to another comma-delimited file. This file contains the columns drug_name, num_prescriber, and total_cost, in that order, 
and the first row is again a header line.

For very large files, the program also provides progress messages every million records during all loops. Progress statements are also
printed after successfully reading in the file, creating the dictionary of drugs (with prescriber and total cost information), 
converting the dictionary to a list, and printing the output file.

# Error Checking
- File reading: If the input file has the incorrect number of columns, the program exits with an error message.
- Drug names: All drug name strings are converted to all uppercase before being set as dictionary keys to ensure case-insensitivity.
- Prescriber IDs: IDs are converted to integers from the read-in string values to ensure both the correct file format (code is 
  non-functional if IDs cannot be converted to integers) and good comparisions between records.
- Total Cost: Costs are converted to floats from the read in string values to ensure the correct file format (code is 
  non-functional if costs cannot be converted to floats).
- Prescriber Name: Not required, since name is not used for any kind of calculations or comparisions.