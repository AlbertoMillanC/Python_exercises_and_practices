from Screenshot import Screenshot
from selenium import webdriver

ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()