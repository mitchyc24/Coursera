'''
https://www.coursera.org/learn/python-data/gradedLti/hYbVS/assignment-10-2

10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour 
of the day for each of the messages. You can pull the hour out from the 'From ' line by finding 
the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
name = r"Python_for_Everyone_Specialty\Python_Data_Structures\mbox-short.txt"
handle = open(name)


times = {}

for line in handle:
    if line.startswith("From"):
        words = line.split()
        try:
            hour = words[5][:2]
            times[hour] = times.get(hour, 0) + 1
            hours = sorted(times.items())
        except:
            pass
        
for k,v in hours:
    print(k,v)
        
