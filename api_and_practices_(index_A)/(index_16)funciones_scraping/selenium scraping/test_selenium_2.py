import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Inicializamos el driver de Chrome
driver = webdriver.Chrome()

# Abrimos la página de inicio de sesión de The Internet
driver.get("https://the-internet.herokuapp.com/login")

time.sleep(15)

# Ingresamos las credenciales de inicio de sesión
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID,"password")
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")

# Hacemos clic en el botón de inicio de sesión
driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()

# Verificamos que se inició sesión correctamente
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".flash.success"), "You logged into a secure area!")
)

# Navegamos a la página de WYSIWYG Editor
driver.get("https://the-internet.herokuapp.com/tinymce")

# Obtenemos el iframe que contiene el editor WYSIWYG
editor_frame = driver.find_element(By.ID,"mce_0_ifr")

# Cambiamos al iframe
driver.switch_to.frame(editor_frame)

# Escribimos texto en el editor
editor = driver.find_element_by_css_selector("#tinymce")
editor.send_keys("¡Hola, mundo!")

# Cambiamos de vuelta al contenido principal
driver.switch_to.default_content()

# Cerramos sesión
driver.find_element_by_css_selector(".icon-2x.icon-signout").click()

# Verificamos que se cerró sesión correctamente
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".flash.success"), "You logged out of the secure area!")
)

# Cerramos el driver
driver.quit()
