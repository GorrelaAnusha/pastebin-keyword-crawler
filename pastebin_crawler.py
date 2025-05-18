import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

# Constants
BASE_ARCHIVE_URL = "https://pastebin.com/archive"
RAW_URL_FORMAT = "https://pastebin.com/raw/{}"
KEYWORDS = ["crypto", "bitcoin", "ethereum", "blockchain", "t.me"]
OUTPUT_FILE = "keyword_matches.jsonl"

# Function to get Paste IDs from archive
def get_paste_ids():
    print("Fetching paste IDs from archive...")
    response = requests.get(BASE_ARCHIVE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("table.maintable a")
    paste_ids = [link["href"].strip("/").split("/")[-1] for link in links if "/archive" not in link["href"]]
    return paste_ids[:30]

# Function to fetch raw paste content
def fetch_paste_content(paste_id):
    url = RAW_URL_FORMAT.format(paste_id)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return ""
    except:
        return ""

# Function to check and collect matching pastes
def crawl_and_collect():
    results = []
    paste_ids = get_paste_ids()

    for paste_id in paste_ids:
        print(f"Checking paste ID: {paste_id}")
        content = fetch_paste_content(paste_id)
        found_keywords = [kw for kw in KEYWORDS if kw.lower() in content.lower()]

        if found_keywords:
            result = {
                "source": "pastebin",
                "context": f"Found crypto-related content in Pastebin paste ID {paste_id}",
                "paste_id": paste_id,
                "url": RAW_URL_FORMAT.format(paste_id),
                "discovered_at": datetime.utcnow().isoformat() + "Z",
                "keywords_found": found_keywords,
                "status": "pending"
            }
            results.append(result)
        else:
            print(f"No keywords found in {paste_id}")

        time.sleep(1.5)  # Rate limiting

    # Write results to .jsonl
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for item in results:
            f.write(json.dumps(item) + "\n")

    print(f"\n✅ Finished. {len(results)} matching pastes saved to '{OUTPUT_FILE}'.")

# Run the function
crawl_and_collect()
