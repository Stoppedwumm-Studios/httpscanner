import os

import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scan_website(url, depth=0,results=[]):
    print(depth)
    if depth >= 5:
        return

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parse')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                results.append({
                    "parent_url": url,
                    "child_url": href
                })

                child_url = urljoin(url, href)
                depth += 1
                scan_website(child_url, depth, results)

    else:
        print(f"Error: Could not access website: {url}")

if __name__ == "__main__":
    
    depth=0
    url = "https://wikipedia.org/"
    results = []
    scan_website(url, results=results)

    with open('scan_results.json', 'w') as outfile:
        json.dump(results, outfile)

    print("Scan results saved to scan_results.json")
