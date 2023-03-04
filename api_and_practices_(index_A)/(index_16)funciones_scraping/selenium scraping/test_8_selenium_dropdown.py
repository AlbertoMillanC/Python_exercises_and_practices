from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.colombialoterias.com/loteria-de-boyaca/")

select = Select(driver.find_element(By.CSS_SELECTOR, "#rrm-draws-datetime-list"))
for option in select.options:
    print(option.text)
    
    # Obtener el contenido HTML de la página
    html_content = driver.find_element(By.CSS_SELECTOR, "body").get_attribute("innerHTML")
    
    # Escribir el contenido HTML en un archivo de texto
    with open(f"{option.text}.txt", "w") as f:
        f.write(html_content)

driver.quit()
