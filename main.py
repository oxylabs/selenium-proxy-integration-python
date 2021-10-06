import time
from selenium import webdriver
# A package to have a chromedriver always up-to-date.
from webdriver_manager.chrome import ChromeDriverManager
from proxies import chrome_proxy

USERNAME = "your_username"
PASSWORD = "your_password"
HOST = "pr.oxylabs.io"
PORT = 7777
# Specify country code if you want proxies from a single country, e.g. `US`.
# Otherwise - set the variable to `None`.
COUNTRY = "US"

options = webdriver.ChromeOptions()
proxy_ext = chrome_proxy(USERNAME, PASSWORD, HOST, PORT, COUNTRY)
options.add_extension(proxy_ext)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    driver.get("https://ip.oxylabs.io/")
    time.sleep(5)
finally:
    driver.quit()
