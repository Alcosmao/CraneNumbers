from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime
import re
from time import sleep
from random import randint
import pandas as pd

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}


def ExportDataToDataFrame(CranesNickFinder, CranesDateFinder, CranesNumberFinder):
    pass
    # with open('dataFrame.txt', 'a') as file:
        # file.write()
    col = ['Nick', 'Date', 'Crane Number']
    bscList = []
    lstToAdd = [CranesNickFinder, CranesDateFinder, CranesNumberFinder]
    bscList.extend(lstToAdd)
    print(bscList)
    # bscList.append(lstToAdd)
    # dataFrame = pd.DataFrame(bscList, columns=col)
    # dataFrame = dataFrame.append(pd.DataFrame([lstToAdd], columns=dataFrame.columns), ignore_index=True)
    # print(dataFrame)


def CranesNumberFinder(CranesCountFinderNumber):
    try:
        CraneRegex = r"(Razem|Suma|=).?.? (\d+)"
        CranesExactNumber = re.findall(CraneRegex, CranesCountFinderNumber)
        CranesValue = CranesExactNumber[0]
        # CranesExactLen = len(CranesExactNumber)
        # CranesValue = CranesExactNumber[0] if CranesExactLen == 1 else CranesExactNumber[-1]
        print("Number of cranes at the post time: " + str(CranesValue[1]))
        return CranesValue[1]
    except:
        print("Wrong value")
####
# (?:Razem|Suma|=):? (\d+)
###
# (Razem|Suma|=).?.? (\d+)
###


def CranesDateFinder(CranesCountFinder):
    CranesFindDate = CranesCountFinder.find('div', class_='message-attribution-main')
    CranesPostDate = CranesFindDate.find('time')['data-date-string']
    print("Date of the post: " + CranesPostDate)
    return CranesPostDate


def CranesNickFinder(CranesCountFinder):
    CranesPostNickFinder = CranesCountFinder.find('a', class_='username').text
    print("This data is provided by: " + CranesPostNickFinder)
    return CranesPostNickFinder


WordRange = ["Razem", "Suma", "="]
WordRangeRazem = "Razem"
WordRangeSuma = "Suma"
HtmlText = 'https://www.skyscrapercity.com/threads/wroc%C5%82aw-%C5%BBurawie-w-naszym-mie%C5%9Bcie.503734/page-'
Repeat = True
while Repeat:
    for page in range(2, 183):
        req = requests.get(HtmlText + str(page))
        soup = BeautifulSoup(req.text, 'lxml')
        CranesCountFinders = soup.find_all('article', class_='message message--post js-post js-inlineModContainer california-message')
        for CranesCountFinder in CranesCountFinders:
            CranesCountFinderNumber = CranesCountFinder.find('div', class_='bbWrapper').text
            if any(CraneNumber in CranesCountFinderNumber for CraneNumber in WordRange):
                CranesNickFinder(CranesCountFinder)
                CranesDateFinder(CranesCountFinder)
                CranesNumberFinder(CranesCountFinderNumber)
                print("This is page number: " +str(page))
                print("#@"*30)
                ExportDataToDataFrame(CranesNickFinder, CranesDateFinder, CranesNumberFinder)
        sleep(randint(2, 5))
    Repeat = input("Ask again: Yes/ No: ")
    if Repeat != "Yes":
        break
print("Good bye.")


