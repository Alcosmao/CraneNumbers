from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime
import re
from time import sleep
from random import randint

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}


def PrintingCraneInformation(CranesExactNumber):
    print("Number of cranes at the post time: " + CranesExactNumber)
    print("#"*100)


def CraneNumberFinder(CranesCountFinderNumber):
    pass


def CranesDateFinder(CranesCountFinder):
    CranesFindDate = CranesCountFinder.find('div', class_='message-attribution-main')
    CranesPostDate = CranesFindDate.find('time')['data-date-string']
    print("Date of the post: " + CranesPostDate)


def CranesNickFinder(CranesCountFinder):
    CranesPostNickFinder = CranesCountFinder.find('a', class_='username').text
    print("This data is provided by: " + CranesPostNickFinder)



WordRange = ["Suma", "Razem", "="]
HtmlText = 'https://www.skyscrapercity.com/threads/wroc%C5%82aw-%C5%BBurawie-w-naszym-mie%C5%9Bcie.503734/page-'
Repeat = True
while Repeat:
    for page in range(2, 4):
        req = requests.get(HtmlText + str(page))
        soup = BeautifulSoup(req.text, 'lxml')
        CranesCountFinders = soup.find_all('article', class_='message message--post js-post js-inlineModContainer california-message')
        for CranesCountFinder in CranesCountFinders:
            CranesCountFinderNumber = CranesCountFinder.find('div', class_='bbWrapper').text
            if any(CraneNumber in CranesCountFinderNumber for CraneNumber in WordRange):
                CranesNickFinder(CranesCountFinder)
                CranesDateFinder(CranesCountFinder)
                CranesExactNumber = re.findall(r"\d+", CranesCountFinderNumber)
                CranesExactNumber = str(max(map(int, CranesExactNumber), default=0))
                PrintingCraneInformation(CranesExactNumber)
        #sleep(randint(2, 5))
    Repeat = input("Ask again: Yes/ No: ")
    if Repeat != "Yes":
        break
print("Good bye.")

lambda x: "Razem" or "Suma" or "=" in x

