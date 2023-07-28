# Selenium

---

- [Selenium github](https://github.com/SeleniumHQ/selenium/tree/trunk/py)
- [Selenium pypi.org](https://pypi.org/project/selenium/)
    - `pip install -U selenium`

## Docs

[Selenium with Python](https://selenium-python.readthedocs.io/index.html)

- [Locating Elements (find by...)](https://selenium-python.readthedocs.io/locating-elements.html)
```python
ID = "id"
NAME = "name"  # attribute "name"="some attr name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

About [XPath](https://developer.mozilla.org/en-US/docs/Web/XPath)

```python
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://site.com")
title = driver.find_element(By.CSS_SELECTOR, "h1[data-product-title]")
print(title.text)
```
