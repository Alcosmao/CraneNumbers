from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

HtmlText = requests.get('https://www.skyscrapercity.com/threads/wroc%C5%82aw-%C5%BBurawie-w-naszym-mie%C5%9Bcie.503734/page-4').text
Soup = BeautifulSoup(HtmlText, 'lxml')
CranesCountFinder = Soup.find('article', class_='message message--post js-post js-inlineModContainer california-message')
CranesPostNickFinder = CranesCountFinder.find('a', class_ ='username').text
print("This data is provided by: " + CranesPostNickFinder)
CranesCountFinderNumber = Soup.find('div', class_='bbWrapper')
print(CranesCountFinderNumber)


# DateFinder = re.search(r'\D{3} \d+, \d{4}', CranesCountNickAndDateFinder)
# Date = datetime.strptime(DateFinder, '%b %-d %Y').date()
# for DataFinder in CranesCountFinder:
#     print(DataFinder)

