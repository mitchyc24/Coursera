'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute
the average of those values and produce an output as shown below. Do not use the sum() function 
or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing 
below enter mbox-short.txt as the file name.

https://www.coursera.org/learn/python-data/gradedLti/IlVLg/assignment-7-2
'''


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fname = r"Python_for_Everyone_Specialty\Python_Data_Structures\mbox-short.txt"
fh = open(fname)

count = 0
tot = 0 

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line.rstrip())
    count += 1
    index = line.find(':')

    try:
        tot += float(line[index+1:])
    except:
        print("Unexpected Error")
        break

avg = tot/count
print("Average spam confidence:", avg)



print("Done")

