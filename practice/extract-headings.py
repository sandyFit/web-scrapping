from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import ssl
from bs4 import BeautifulSoup
import random

# --- SSL Context (ignore certificate errors) ---
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# --- User-Agent Rotation ---
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
    '(KHTML, like Gecko) Version/16.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
]

headers = {'User-Agent': random.choice(user_agents)}

# --- Input URL ---
url = input('Enter URL: ').strip()
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url  # fallback to http

try:
    req = Request(url, headers=headers)
    html = urlopen(req, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    results = []
    summary = {}

    print("\n=== Headings Extracted ===\n")

    for level in range(1, 7):
        headings = soup.find_all(f'h{level}')
        summary[f'h{level}'] = len(headings)
        
        for i, heading in enumerate(headings, start=1):
            text = heading.get_text(strip=True)
            line = f"H{level}-{i}: {text}"
            print(line)
            print('-' * 40)
            results.append(line)

    print("\n=== Summary ===")
    for level, count in summary.items():
        print(f"Total {level.upper()}: {count}")

    # Save results
    with open("headings_report.txt", "w", encoding="utf-8") as f:
        f.write("Headings Report\n\n")
        f.write("\n".join(results))
        f.write("\n\nSummary:\n")
        for level, count in summary.items():
            f.write(f"{level.upper()}: {count}\n")

    print("\n✅ Results saved to headings_report.txt")

except HTTPError as e:
    print(f"❌ HTTP error {e.code}: {e.reason}")
except URLError as e:
    print(f"❌ Failed to reach the server: {e.reason}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
