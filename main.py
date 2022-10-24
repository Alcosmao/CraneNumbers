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

HtmlText = requests.get('https://www.skyscrapercity.com/threads/wroc%C5%82aw-%C5%BBurawie-w-naszym-mie%C5%9Bcie.503734/page-2').text
Soup = BeautifulSoup(HtmlText, 'lxml')
CranesCountFinder = Soup.find('div', class_='message-inner')
CranesCountNickAndDateFinder = CranesCountFinder.find('div', class_='message-userContent').text
DateFinder = re.search(r'\D{3} \d{2}, \d{4}', CranesCountNickAndDateFinder)
Date = datetime.strptime(DateFinder, '%m-%d-%Y').date()
print(DateFinder)
# for DataFinder in CranesCountFinder:
#     print(DataFinder)

