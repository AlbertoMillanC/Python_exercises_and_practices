from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

try:
    # Inicializar el driver de Chrome
    driver = webdriver.Chrome()

    # Abrir la página de la aplicación
    driver.get("https://the-internet.herokuapp.com/")

    # Hacer clic en el enlace "Dropdown"
    dropdown_link = driver.find_element(By.LINK_TEXT, "Dropdown")
    dropdown_link.click()

    # Esperar a que se cargue la página
    time.sleep(2)

    # Seleccionar una opción del menú desplegable
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    options = dropdown.options
    for i in range(len(options)):
        dropdown.select_by_index(i)
        selected_option = dropdown.first_selected_option.text
        print(f"Opción seleccionada: {selected_option}")
        time.sleep(1)

    # Cerrar el navegador
    driver.quit()

except NoSuchElementException as e:
    print("No se encontró el elemento:", e)

except ElementNotInteractableException as e:
    print("El elemento no es interactuable:", e)

except Exception as e:
    print("Ocurrió una excepción no identificada:", e)