import urllib.request

wiki = "https://es.wikipedia.org/wiki/Anexo:Capitales_de_Estado"

# Build request with headers
# wikipedia blocks requests without a User-Agent header
# Add a User-Agent header so the request looks like it’s coming from a normal browser
req = urllib.request.Request(
    wiki,
    headers={"User-Agent": "Mozilla/5.0"}
)

# Open the URL with the request
# with... ensures the connection is closed after reading.
with urllib.request.urlopen(req) as response:
    for line in response:
        print(line.decode("utf-8").strip())
