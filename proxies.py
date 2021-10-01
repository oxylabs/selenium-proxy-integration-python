import zipfile
from typing import Optional

MANIFEST_JSON = """
    {
      "version": "1.0.0",
      "manifest_version": 2,
      "name": "Oxylabs Selenium Proxy Integration",
      "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
      ],
      "background": {
        "scripts": ["background.js"]
      },
      "minimum_chrome_version":"22.0.0"
    }
    """

BACKGROUND_JS = """
    var config = {
      mode: "fixed_servers",
      rules: {
        singleProxy: {
          scheme: "http",
          host: "%s",
          port: %d,
        },
        bypassList: ["localhost"]
      }
    };
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    function callbackFn(details) {
      return {
        authCredentials: {
          username: "customer-%s",
          password: "%s",
        }
      };
    }
    chrome.webRequest.onAuthRequired.addListener(
      callbackFn,
      {urls: ["<all_urls>"]},
      ['blocking']
    );
"""


def chrome_proxy(user: str, password: str, host: str, port: int, country: Optional[str] = None):
    if country:
        user = f"{user}-cc-{country}"

    bg = BACKGROUND_JS % (
        host,
        port,
        user,
        password,
    )

    ext = "proxy_extension.zip"
    with zipfile.ZipFile(ext, "w") as zp:
        zp.writestr("manifest.json", MANIFEST_JSON)
        zp.writestr("background.js", bg)

    return ext
