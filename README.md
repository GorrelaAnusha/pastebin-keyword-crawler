# pastebin-keyword-crawler
## Description
This Python script scrapes Pastebin’s public archive for pastes containing cryptocurrency-related keywords (like "crypto", "bitcoin", "ethereum") or Telegram links ("t.me"). It extracts relevant pastes and saves their info in a JSONL file.

## Setup Instructions
1. Clone the repository or download the files.
2. Install required libraries:
pip install requests beautifulsoup4

3. Run the script:
python pastebin_crawler.py

## Usage
Run the script from the command line:
python pastebin_crawler.py

It will crawl the latest 30 pastes on Pastebin and save those containing keywords to `keyword_matches.jsonl`.


https://github.com/GorrelaAnusha/pastebin-keyword-crawler/blob/main/Screenshot.png

## Sample Output
An example JSON entry saved in `keyword_matches.jsonl`:
```json
{
  "source": "pastebin",
  "context": "Found crypto-related content in Pastebin paste ID abc123",
  "paste_id": "abcdefg11",
  "url": "https://pastebin.com/raw/abcdefg11",
  "discovered_at": "2025-05-12T10:00:00Z",
  "keywords_found": ["crypto", "bitcoin"],
  "status": "pending"
}

