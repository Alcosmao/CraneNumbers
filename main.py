from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime
import re
from time import sleep
from random import randint
import pandas as pd
import csv

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}


def ExportDataToDataFrame(CranesCountFinder, CranesCountFinder2, CranesCountFinderNumber):
    try:
            x = CranesNickFinder(CranesCountFinder)
            y = CranesDateFinder(CranesCountFinder2)
            z = CranesNumberFinder(CranesCountFinderNumber)
            for condition in z:
                if condition is not None:
                    lst = [x, y, z]
                    print(lst)
                    # header = ['Nick', 'Date', 'CraneNumber']
                    with open('newData', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(lst)
                else:
                    continue
    except:
        print("Error")

    # col = ['Nick', 'Date', 'Crane Number']
    # dataFrame = pd.DataFrame([generalList], columns=col)
    # dataFrame = dataFrame.append(pd.DataFrame(lst, columns=col), ignore_index=True)
    # print(dataFrame)


def createCsvFile():
    header = ['Nick', 'Date', 'CraneNumber']
    with open('newData', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(header)


def CranesNumberFinder(CranesCountFinderNumber):
    try:
        CraneRegex = r"(Razem|Suma|=).?.? (\d+)"
        CranesExactNumber = re.findall(CraneRegex, CranesCountFinderNumber)
        CranesValue = CranesExactNumber[0]
        # print("Number of cranes at the post time: " + str(CranesValue[1]))
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
    # print("Date of the post: " + CranesPostDate)
    return CranesPostDate


def CranesNickFinder(CranesCountFinder):
    CranesPostNickFinder = CranesCountFinder.find('a', class_='username').text
    # print("This data is provided by: " + CranesPostNickFinder)
    return CranesPostNickFinder


def CraneGatherData():
    WordRange = ["Razem", "Suma", "="]
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
                    ExportDataToDataFrame(CranesCountFinder, CranesCountFinder, CranesCountFinderNumber)
                    print("This is page number: " +str(page))
                    print("#@"*30)
            sleep(randint(2, 5))
        Repeat = input("Ask again: Yes/ No: ")
        if Repeat != "Yes":
            break
    print("Good bye.")


def Main():
    # createCsvFile()
    CraneGatherData()
    ExportDataToDataFrame()
    # saveDataToDataFrame(ExportDataToDataFrame)


Main()



# if __name__ == "__main__":
#     main()
