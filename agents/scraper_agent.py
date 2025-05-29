import requests
from bs4 import BeautifulSoup

def fetch_company_filings(url):
    """Scrape financial filings efficiently."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    reports = soup.find_all("div", class_="filing-summary")
    return [report.text for report in reports]