import urllib.request
import ssl
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Helps combine base URL with relative links

# --- SSL Setup ---
# Create an SSL context to ignore certificate errors (useful for sites with invalid/expired SSL certificates).
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# --- Input URL ---
# Ask the user to enter a URL (e.g., https://www.python.org).
url = input('Enter - ')

# --- Add User-Agent Header ---
# Pretend to be a browser (common trick to avoid 403 errors)
headers = {
    'User-Agent': 'Mozzila/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)

# --- Fetch HTML ---
# Open the URL using urllib, read the raw HTML, and store it in the 'html' variable.
# 'context=ctx' ensures SSL certificate issues are ignored.
html = urllib.request.urlopen(req, context=ctx).read()

# --- Parse HTML ---
# Create a BeautifulSoup object to parse the HTML content.
# Note: Correct parser name is "html.parser" (not "html-parser").
soup = BeautifulSoup(html, 'html.parser')

# --- Find All Links ---
# Retrieve all <a> tags (anchor tags) from the parsed HTML.
tags = soup('a')

# --- Extract and Print HREF Attributes ---
# Loop through each <a> tag and print the 'href' attribute (the link URL).
# If an <a> tag has no 'href', print None.
for tag in tags:
    href = tag.get('href', None)
    if href:
        absolute_url = urljoin(url, href)  # Convert relative urls to absolute
        print(tag)
        print(absolute_url)
        print('=================================\n')


