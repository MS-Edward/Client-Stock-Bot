import bs4
import requests
import re
import EmailService
import sys

#SBot role is as follows:
#Given a ticker symbol, SBot will copy the corresponding Reuters financial HTML page. It will then proceed to parse the information into a readable format.
class SBot:

    def __init__(self, stockName):
        self.stockName = stockName

    def retrieveStockInformation(self):
        request = requests.get("http://www.reuters.com/finance/stocks/overview/" + self.stockName)
        request.raise_for_status()
        htmlPage = bs4.BeautifulSoup(request.text, 'html.parser')
        contentBlock = htmlPage.select('html body.BETAUS div#content div.section div.sectionContent div#sectionHeader div.quoteCont div.module div.moduleBody div#headerQuoteContainer div.sectionQuote.nasdaqChange div.sectionQuoteDetail span')
        return contentBlock

    def parseContent(self,contentBlock):
        i = 0
        for string in map(str, contentBlock):
            contentBlock[i] = re.sub('<[^>]+>', '', string).strip()
            i += 1
        return contentBlock

    def getStockInformation(self):
        parsedStockInformation = self.parseContent(self.retrieveStockInformation())
        return parsedStockInformation[0] + '\n' + parsedStockInformation[1] + ' ' + parsedStockInformation[2] + ' ' + parsedStockInformation[3]


sys.argv
if len(sys.argv) > 1:
    stockBot = SBot(''.join(sys.argv[1:]))
else:
    stockBot = SBot('HD')

newEmail = EmailService.Email("Stock Quote", stockBot.getStockInformation(), "Automated Service")
print(stockBot.getStockInformation())
