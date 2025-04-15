import requests
from bs4 import BeautifulSoup

def fetch_writeup_content(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text(separator='\n').strip()
    except requests.RequestException:
        pass
    return "Not extracted"

def scrape_ctf_writeups(base_url, num_pages):
    dataset = []

    for page in range(1, num_pages + 1):
        page_url = f"{base_url}?page={page}"
        res = requests.get(page_url)
        if res.status_code != 200:
            print(f"Failed to load page {page}")
            continue

        soup = BeautifulSoup(res.text, 'html.parser')
        rows = soup.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 3:
                continue

            ctf_name = cols[0].text.strip()
            challenge_name = cols[1].text.strip()
            year = cols[2].text.strip()
            link_tag = row.find('a', href=True)

            if link_tag:
                href = link_tag['href']
                full_url = href if href.startswith("http") else f"https://ctftime.org{href}"
                content = fetch_writeup_content(full_url)

                dataset.append({
                    "title": challenge_name,
                    "tags": ctf_name,
                    "year": year,
                    "url": full_url,
                    "content": content
                })
    return dataset
