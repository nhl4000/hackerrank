import urllib.request
import re
start = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html"
path = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/"

visited = set("qds")
secrets = []
contents = urllib.request.urlopen(start).read().decode('utf-8')
secret = re.findall("Secret Phrase: </b>(.*)</font>", contents)
if (len(secret) == 1):
    secrets.append(secret[0])
links = re.findall("href=(.*).html>", contents)

index = 0
for link in links:
    if link in visited:
        continue
    else:
        print("Visiting "+link)
        visited.add(link)
        contents = urllib.request.urlopen(path+link+".html").read().decode('utf-8')
        secret = re.findall("Secret Phrase: </b>(.*)</font>", contents)
        if (len(secret) == 1):
            secrets.append(secret[0])
        links += re.findall("href=(.*).html>", contents)

print("\n".join(secrets))