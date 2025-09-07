import urllib.request

request_url = urllib.request.urlopen('https://www.ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt')

shakespeare_data = []
for line in request_url:
    shakespeare_data.append(line.decode().strip())
    print(shakespeare_data)
