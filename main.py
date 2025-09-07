from urllib.request import Request, urlopen
import gzip

req = Request("http://www.debian.org")
# The Accept-Encoding header tells the server what compression formats the client can understand.
# gzip = a widely used compression format that makes text, JSON, and files smaller 
# gzip saves bandwidth, speeds up transfer, and reduces storage.
req.add_header("Accept-Encoding", "gzip") # the same information takes up much fewer bytes.
response = urlopen(req)

# Read raw bytes
raw_data = response.read()

# Check headers
encoding = response.headers.get("Content-Encoding")

if encoding == "gzip":
    # Decompress if gzipped
    content = gzip.decompress(raw_data).decode("utf-8")
else:
    # Otherwise, just decode normally
    content = raw_data.decode("utf-8")

print(content)
