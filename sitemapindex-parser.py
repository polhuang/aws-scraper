import xml.etree.ElementTree as ET
import json
import requests

# Read main.xml file, which contains sitemap index from https://docs.aws.amazon.com/sitemap_index.xml, with SDK sitemaps removed
with open("main.xml", "r") as xml_file:
    sitemap_index_data = xml_file.read()

# Function to extract URLs from xml content    
def extract_urls_from_xml(xml_content):
    root = ET.fromstring(xml_content)
    return [element.text for element in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

sitemap_index_urls = extract_urls_from_xml(sitemap_index_data)

all_urls = []

for url in sitemap_index_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        xml_content = response.text

        # Extract URLs from each sitemap in sitemap index, add to list of all URLs
        extracted_urls = extract_urls_from_xml(xml_content)
        all_urls.extend(extracted_urls)

        # Print the extracted URLs
        for extracted_url in extracted_urls:
            print(extracted_url)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching XML from {url}: {e}")

with open("html_urls.json", "w") as json_file:
    json.dump(all_urls, json_file, indent=2)
