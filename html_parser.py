import os
import requests
from bs4 import BeautifulSoup
import json

# Read list of aggregate html files from AWS sitemaps
with open('html_urls.json', 'r') as json_file:
    urls = json.load(json_file)

# Create a folder "docs"
if not os.path.exists("aws-docs"):
    os.makedirs("aws-docs")

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text

            # Create filename from url
            filename = os.path.join("aws-docs", url.split("//")[-1].replace("/", "_") + ".html")

            # Write content to file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)

            print(f"Content from {url} saved in {filename}\n")

        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching content from {url}: {e}\n")


        
