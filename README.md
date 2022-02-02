# Oxylabs’ Residential Proxies integration with Selenium in Python

[<img src="https://img.shields.io/static/v1?label=&message=Python&color=brightgreen" />](https://github.com/topics/python) [<img src="https://img.shields.io/static/v1?label=&message=Selenium&color=orange" />](https://github.com/topics/selenium) [<img src="https://img.shields.io/static/v1?label=&message=Web-Scraping&color=yellow" />](https://github.com/topics/web-scraping) [<img src="https://img.shields.io/static/v1?label=&message=Rotating%20Proxies&color=blueviolet" />](https://github.com/topics/rotating-proxies)

## Requirements

For the integration to work, you'll need to install
[Selenium Wire](https://github.com/wkeeling/selenium-wire) 
to extend Selenium’s Python bindings as implementing proxies
that require authentication using default Selenium module 
complicates the process too much.

You can do it using `pip` command:
```bash
pip install selenium-wire
```

Another recommended package is `webdriver-manager`. It simplifies the management
of binary drivers for different browsers, so you don't need to manually download
a new version of a web driver after each update. Visit the 
[official project directory](https://pypi.org/project/webdriver-manager/) on pypi to
find out more information. 

You can install the following using `pip` as well:
```bash
pip install webdriver-manager
```

Required version of Python: `Python 3.5` (or higher)

## Proxy Authentication

For proxies to work, you'll need to specify your account credentials inside 
the [main.py](https://github.com/oxylabs/selenium-proxy-integration/blob/main/main.py) file.

```python
USERNAME = "your_username"
PASSWORD = "your_password"
ENDPOINT = "pr.oxylabs.io:7777"
```

Adjust the `your_username` and `your_password` value fields with the username and password of 
your Oxylabs account.

## Testing Proxy Connection

To see if the proxy is working, try visiting [ip.oxylabs.io](https://ip.oxylabs.io) 
If everything is working correctly, it will return an IP address of a proxy that you're using.

## Full Code
```python
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
# A package to have a chromedriver always up-to-date.
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "your_username"
PASSWORD = "your_password"
ENDPOINT = "pr.oxylabs.io:7777"


def chrome_proxy(user: str, password: str, endpoint: str) -> dict:
    wire_options = {
        "proxy": {
            "http": f"http://{user}:{password}@{endpoint}",
            "https": f"http://{user}:{password}@{endpoint}",
        }
    }

    return wire_options


def execute_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    proxies = chrome_proxy(USERNAME, PASSWORD, ENDPOINT)
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options, seleniumwire_options=proxies
    )
    try:
        driver.get("https://ip.oxylabs.io/")
        return f'\nYour IP is: {driver.find_element(By.CSS_SELECTOR, "pre").text}'
    finally:
        driver.quit()


if __name__ == "__main__":
    print(execute_driver())
```

If you're having any trouble integrating proxies with Selenium and this guide didn't help 
you - feel free to contact Oxylabs customer support at support@oxylabs.io.
