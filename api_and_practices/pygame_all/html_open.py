from Screenshot import Screenshot
from selenium import webdriver

ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/blob/master/Screenshot/Screenshot_Clipping.py"
driver.get(url)

element = driver.find_element_by_class_name('signup-prompt')
img_url = ob.get_element(driver, element, r'.')
print(img_url)

driver.close()

driver.quit()
