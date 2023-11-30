from selenium.webdriver.common.by import By
from seleniumwire import webdriver
# A package to have a chromedriver always up-to-date.
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "your_username"
PASSWORD = "your_password"
ENDPOINT = "pr.oxylabs.io:7777"


def get_chrome_proxy(user: str, password: str, endpoint: str) -> dict:
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
    seleniumwire_options = {
        **get_chrome_proxy(USERNAME, PASSWORD, ENDPOINT),
        "driver_path": ChromeDriverManager().install(),
    }
    driver = webdriver.Chrome(
        options=options,
        seleniumwire_options=seleniumwire_options,
    )
    try:
        driver.get("https://ip.oxylabs.io/")
        return f'\nYour IP is: {driver.find_element(By.CSS_SELECTOR, "pre").text}'
    finally:
        driver.quit()


if __name__ == "__main__":
    print(execute_driver())
