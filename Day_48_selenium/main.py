from selenium.webdriver.common.by import By
from selenium import webdriver

url = "https://ukrainianarmor.com/product/plytonoska-fpc-bez-plyt/?attribute_pa_color=multicam&attribute_pa_size=l"

driver = webdriver.Chrome()
driver.get(url)

title = driver.find_element(By.CSS_SELECTOR, "h1[data-product-title]")
price = driver.find_element(By.CSS_SELECTOR, "div[data-product-price]")
send_by = driver.find_element(By.XPATH, '//*[starts-with(@id, "product")]/div[1]/div[6]/div/div')

print(title.text)
print(price.get_attribute("data-product-price"))
print(send_by.text)

# browser.close()
# browser.quit()
