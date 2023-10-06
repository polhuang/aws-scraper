# aws-scraper
Scrapes AWS documentation into html files

## main.xml
Sitemap index from https://docs.aws.amazon.com/sitemap_index.xml. Removed documentation for AWS SDKs, reducing # of documents from 600k+ to 100k+.

Sitemap index contains a list of xml sitemaps for AWS documentation topics

## sitemapindex-parser.py
Reads the sitemap index and aggregates html files listed within each xml sitemap in main.xml. Outputs to html_urls.json for review.

## html_parser.py
Saves each html document in html_urls.json to "aws-docs" folder.
