import re

name = r"Python_for_Everyone_Specialty\Python_Data_Structures\mbox-short.txt"
handle = open(name)

whole_text = handle.read()

numlist = re.findall(r"[0-9]+:[0-9]+:[0-9]+", whole_text)
emails = re.findall(r"\S+@S+", whole_text)
emails_after_From = re.findall(r"From (\S+@\S+)", whole_text) #Pretty good idea to preface
hostnames = re.findall(r"@([A-Za-z0-9\.]+)", whole_text) #Best so far
domain = re.findall(r"@[^ \n]*", whole_text) #Doesn't quite work


unique_hostnames = []

for item in hostnames:
    if item not in unique_hostnames:
        unique_hostnames.append(item)


# print("emails:", len(emails))
# print("emails after From ", len(emails_after_From))
# print(hostnames)
# print(len(hostnames), len(unique_hostnames),unique_hostnames)
print(domain)