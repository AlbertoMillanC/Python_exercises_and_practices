import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

try:
    # Inicializamos el driver de Chrome
    driver = webdriver.Chrome()

    # Abrimos la página de inicio de sesión de The Internet
    driver.get("https://www.colombialoterias.com/loteria-de-boyaca/")
 
    # Esperar a que cargue el contenido
    time.sleep(0)
   
    
    # # Hacer clic en el enlace "Dropdown"
    dropdown_link = driver.find_element(By.CSS_SELECTOR, "#rrm-draws-datetime-list")
    dropdown_link.click()
   
    # # Seleccionar una opción del menú desplegable
    dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#rrm-draws-datetime-list"))
    options = dropdown.options
    for i in range(len(options)):
        dropdown.select_by_index(i)
        selected_option = dropdown.first_selected_option.text
        dropdown
        print(f"Opción seleccionada: {selected_option}")
        time.sleep(5)
        
    
    # Cerrar el navegador
    driver.quit()

except NoSuchElementException as e:
    print("No se encontró el elemento:", e)

except ElementNotInteractableException as e:
    print("El elemento no es interactuable:", e)

except Exception as e:
    print("Ocurrió una excepción no identificada:", e)
    

       

   

    
    



    


    
 
    
    

    