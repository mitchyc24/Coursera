'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words 
using the split() method. The program should build a list of words. For each word on each line check to 
see if the word is already in the list and if not append it to the list. When the program completes, 
sort and print the resulting words in alphabetical order.

You can download the sample data at http://www.py4e.com/code3/romeo.txt

https://www.coursera.org/learn/python-data/gradedLti/JQjQD/assignment-8-4
'''

fname = input("Enter file name: ")
fname = r"Python_for_Everyone_Specialty\Python_Data_Structures\romeo.txt"
fh = open(fname)
lst = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
