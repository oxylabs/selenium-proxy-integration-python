# Oxylabs’ Residential Proxies integration with Selenium

[<img src="https://img.shields.io/static/v1?label=&message=Python&color=brightgreen" />](https://github.com/topics/python) [<img src="https://img.shields.io/static/v1?label=&message=Selenium&color=orange" />](https://github.com/topics/selenium) [<img src="https://img.shields.io/static/v1?label=&message=Web-Scraping&color=yellow" />](https://github.com/topics/web-scraping) [<img src="https://img.shields.io/static/v1?label=&message=Rotating%20Proxies&color=blueviolet" />](https://github.com/topics/rotating-proxies)

## Requirements
For the integration to work, you'll need to install Selenium on your system. You can do it using `pip` command:
```bash
pip install selenium
```
Another required package is `webdriver-manager`. It's a package that simplifies the management of binary drivers for different browsers, so you don't need to manually download a new version of a web driver after each update. Visit the [official project directory](https://pypi.org/project/webdriver-manager/) on pypi to find out more information. You can install the following using `pip` as well.
```bash
pip install webdriver-manager
```
Required version of Python: `Python 3.5` (or higher)
## Proxy Authentication
For proxies to work, you'll need to specify your account credentials inside the [main.py](https://github.com/oxylabs/selenium-proxy-integration/blob/main/main.py) file.
```python
USERNAME = "your_username"
PASSWORD = "your_password"
HOST = "pr.oxylabs.io"
PORT = 7777
```
Adjust the `your_username` and `your_password` fields with the username and password of your Oxylabs account.
## Country-Specific Entry Node
If you want, you can also specify the entry node of a specific country:
```python
COUNTRY = "US"
```
To do that, adjust the `country` variable to any country that Oxylabs support. You can check out our [documentation](https://developers.oxylabs.io/residential-proxies/#country-specific-entry-nodes) for a complete list of country-specific entry nodes.

## Testing Proxy Connection
You can test proxy connection by visiting https://ip.oxylabs.io/. It will return your current IP address.
```python
try:
    driver.get("https://ip.oxylabs.io/")
    time.sleep(5)
finally:
    driver.close()
```

## Full Code
```python

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from proxies import chrome_proxy

USERNAME = "your_username"
PASSWORD = "your_password"
HOST = "pr.oxylabs.io"
PORT = 7777
COUNTRY = "US"

options = webdriver.ChromeOptions()
proxy_ext = chrome_proxy(USERNAME, PASSWORD, HOST, PORT, COUNTRY)
options.add_extension(proxy_ext)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    driver.get("https://ip.oxylabs.io/")
    time.sleep(5)
finally:
    driver.close()
```
If you're having any trouble integrating proxies with Selenium and this guide didn't help you - feel free to contact Oxylabs customer support at support@oxylabs.io.


