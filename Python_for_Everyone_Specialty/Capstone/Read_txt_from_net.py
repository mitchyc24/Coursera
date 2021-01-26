import socket
from time import sleep
import sys
import re

pattern = re.compile(">(.+)")
site="http://www.py4e.com/"

sys.path.append("Modules")
import my_web_functions
files = []
for f in my_web_functions.text_files_from_site(site):
    files.append(re.findall(pattern,f))
print(files)


for f in files:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(("www.py4e.com", 80))
    cmd = f"GET /{f[0]} HTTP/1.0\r\nHost: www.py4e.com\r\n\r\n".encode()
    print(cmd)
    mysock.send(cmd)

    while True:
        data = mysock.recv(1)
        if(len(data) < 1):break
        try:
            print(data.decode(), end="")
        except:
            print("XXX", end="")
    mysock.close()