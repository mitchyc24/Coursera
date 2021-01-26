
def text_files_from_site(site="http://data.pr4e.org/"):
    import urllib.request
    import re
    myhandle = urllib.request.urlopen(site)
    files = []
    re_files = r"(\S+\.txt)"
    for line in myhandle:
        filenames = re.findall(re_files, line.decode())
        for f in filenames:
            files.append(f)
    return(files)


def files_from_site(site="http://data.pr4e.org/", ext="\w{2,4}"):
    import urllib.request
    import re

    myhandle = urllib.request.urlopen(site)
    files = []
    re_files = r"(\w+\."+ext+")"
    for line in myhandle:
        filenames = re.findall(re_files, line.decode())
        for f in filenames:
            if f not in files:
                files.append(f)
    return(files)
