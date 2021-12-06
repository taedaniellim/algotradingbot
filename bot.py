from selenium import webdriver
import time

# Locating path to directory of the chromedriver.exe file
PATH = "/Users/daniellim/github/algotradingbot/chromedriver"
# Set up the driver using chrome
web = webdriver.Chrome(PATH)
# Accessing church's homepage
web.get('https://www.barchart.com/etfs-funds/quotes/SPY/price-history/historical')






