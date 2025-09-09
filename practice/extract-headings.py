from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# --- User-Agent Header ---
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36'
}

# Input url
url = input('Enter url: ')
req = Request(url, headers=headers)

html = urlopen(req, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Find all headings in the body (h1, h2, h3, ...)
for level in range(1, 7):
    for heading in soup.find_all(f'h{level}'):
        print(f'H{level}: {heading.get_text(strip=True)}')

