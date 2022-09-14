from configs import cliente
from selenium.webdriver.common.by import By
from controladores import log_controller


class PantallaPrincipal():
    
    # Se obtienen el driver disponible
    driver = cliente.obtener_driver()

    #Elementos de la pagina
    dropdown_rol = "//select[@id='roles']"
    btn_establecer_rol = "//a[@id='imgBtn0']"

    def selecciona_rol(self, rol):
        #self.driver.switch_to.frame("mainFrameSet")
        self.driver.switch_to.frame("welcome_banner")
        seleccion_rol_elements = self.driver.find_element(By.XPATH, self.dropdown_rol)
        seleccion_rol_elements.click()
        seleccion_rol_elements.send_keys(rol)
        self.driver.switch_to.default_content()
        log_controller.log_info(f"Se selecciono el rol -> {rol}")


    def presionar_boton_establece_rol(self):
        self.driver.switch_to.frame("welcome_banner")
        btn_establecer_rol = self.driver.find_element(By.XPATH, self.btn_establecer_rol)
        btn_establecer_rol.click()
        self.driver.switch_to.default_content()