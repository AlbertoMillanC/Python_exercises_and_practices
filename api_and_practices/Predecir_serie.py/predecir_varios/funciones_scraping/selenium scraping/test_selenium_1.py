from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Abrir la página web
url = 'https://www.colombialoterias.com/loteria-de-boyaca/'
driver.get(url)

# Esperar a que el botón se vuelva clickeable
boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="boton-cargar-datos"]')))

# Presionar el botón
boton.click()

# Esperar a que los datos se carguen
datos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="datos-cargados"]')))

# Extraer los datos y hacer el scraping
datos_extraidos = datos.text
# ...

# Cerrar el navegador
driver.quit()
