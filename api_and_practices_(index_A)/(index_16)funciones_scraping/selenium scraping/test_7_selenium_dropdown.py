from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.colombialoterias.com/loteria-de-boyaca/")

select = Select(driver.find_element(By.CSS_SELECTOR, "#rrm-draws-datetime-list"))
for option in select.options:
    print(option.text)