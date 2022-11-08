from Screenshot import Screenshot
from selenium import webdriver

ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3"
driver.get(url)
Hide_elements = ['class=avatar width-full height-full avatar-before-user-status']  # Use full class name
img_url = ob.full_Screenshot(driver, save_path=r'.', elements=Hide_elements, image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()

