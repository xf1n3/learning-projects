import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Apple_Inc"

headers = {
    "User-Agent": "PythonScraper/1.0 (educational project)"
}

response = requests.get(url, headers=headers)
html_content = response.text

if response.status_code == 200:
    print("Успех")
else:
    print("Error1")

soup = BeautifulSoup(html_content, "html.parser")

headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3'])]
paragraphs = [p.text.strip() for p in soup.find_all("p")]
links = [a['href'] for a in soup.find_all("a", href = True)]
infobox = soup.find('table', class_ = 'infobox')
if infobox:
    rows = infobox.find_all('tr')
    data = {}
    for row in rows:
        header = row.find('th')
        value = row.find('td')
        if header and value:
            data[header.text.strip()] = value.text.strip()
else:
    print("None")

table = pd.DataFrame(list(data.items()), columns = ["Key", "Value"])
print(table)
table.to_excel("apple_inc_summary_table.xlsx")