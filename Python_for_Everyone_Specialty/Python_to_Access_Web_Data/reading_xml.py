'''
Welcome Mitchell Carroll from Using Python to Access Web Data

Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_850258.xml (Sum ends with 89)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
'''

def main():
    xml_to_parse = get_xml()
    xml_read = read_xml(xml_to_parse)
    total = count_from_xml(xml_read)
    print(total)

def get_xml(xml_str=None):
    import urllib.request
    if xml_str == None:
        xml_input = input("Enter Online XML Path: ")
    #Set assignment XML path as default
    if not xml_input: 
        xml_input = "http://py4e-data.dr-chuck.net/comments_850258.xml"
    try:
        xml_to_parse = urllib.request.urlopen(xml_input)
    except:
        exit()
    return xml_to_parse.read()

def read_xml(xml_handle):
    import xml.etree.ElementTree as ET
    xml_read = ET.fromstring(xml_handle.decode())
    return xml_read

def count_from_xml(xml_read):
    total = 0
    lst = xml_read.findall("comments/comment/count")
    for count in lst:
        total += int(count.text)
    return total

def exit():
    import os, sys, time
    count = 3
    while count > 0:
        os.system('cls')
        print("Invalid entry. Exiting in",count)
        count -= 1
        time.sleep(1)
    os.system('cls')
    sys.exit()

if __name__ == "__main__":
    main()