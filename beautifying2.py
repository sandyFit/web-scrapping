from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import ssl

# --- SSL Setup ---
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# --- User-Agent Header ---
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36'
}

# --- Input URL ---
url = input('Enter url: ')
req = Request(url, headers=headers)

# --- Fetch and Parse HTML ---
html = urlopen(req, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')  

# --- Prepare storage for numbers ---
all_nums = []

# --- Find all <tr> tags ---
tags = soup('tr')

for tag in tags:
    # Debugging: show tag structure
    print('TAG: ', tag) # full tag
    print('CONTENTS: ', tag.contents[0] if tag.contents else "No contents")
    print('ATTRIBUTES: ', tag.attrs)  # print tag attributes

    # --- Extract ALL Numbers ---
    # Find every number inside the tag
    nums = re.findall(r'[0-9]+', str(tag))
    
    # Convert each number string into float and add to list
    for n in nums:
        all_nums.append(float(n))

# --- Final Sum ---
print("Sum of all numbers:", sum(all_nums))
