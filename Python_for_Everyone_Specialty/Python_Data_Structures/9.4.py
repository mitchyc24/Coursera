'''
https://www.coursera.org/learn/python-data/gradedLti/XLNNf/assignment-9-4

9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number 
of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using
a maximum loop to find the most prolific committer.

'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
name = r"Python_for_Everyone_Specialty\Python_Data_Structures\mbox-short.txt"
handle = open(name)


emails = {}

for line in handle:
    if line.startswith("From:"):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1


email_item = (None, None)
for email, count in emails.items():
    if email_item[0] is None or count > email_item[1]:
        email_item = (email, count)


print(email_item)
