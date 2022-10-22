import bs4
from bs4 import BeautifulSoup
import requests
import lxml
import cloudscraper
import IndeedClient


headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}
scraper = cloudscraper.create_scraper(delay=100000, browser='chrome')
url = "https://www.gov.pl/web/finanse/sprawozdanie-roczne-za-2021"
info = scraper.get(url).text
soup = BeautifulSoup(info, "html.parser")
#soup = soup.find_all('script')
#print(soup)
#page = requests.get(url,headers=headers).content
#soup = BeautifulSoup(requests.get(url, headers=headers, allow_redirects=False).content, 'html.parser')
#soup = bs4.BeautifulSoup(page, 'lxml')
#print(soup)


# HtmlText = requests.get(url).text
# soup = BeautifulSoup(HtmlText, 'lxml')
jobs = soup.find('div', class_ = 'editor-content').text
print(jobs)