'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.

https://www.coursera.org/learn/python-data/gradedLti/dWymU/assignment-6-5
'''
text = "X-DSPAM-Confidence:    0.8475"

index = text.find('.')
num = text[index-1:]

print(float(num))