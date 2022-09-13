from configs import singleton
from selenium import webdriver

def obtener_driver(): 

    driver = None

    if singleton.hay_instancia == True:
        driver = singleton.driver
    else: #Crear el nuevo driver

        chrome_options = webdriver.ChromeOptions()
        driver_path = "/Users/brianruiz/Documents/Brian/chromedriver"
        driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        #Set fullscreen
        driver.set_window_size(1920, 1080)

        singleton.hay_instancia = True
        singleton.driver = driver

       
    return driver

def kill_driver():

    driver_actual = None

    if singleton.hay_instancia == True:
        driver_actual = singleton.driver
        driver_actual.quit()

        singleton.hay_instancia = False
        singleton.driver = None

