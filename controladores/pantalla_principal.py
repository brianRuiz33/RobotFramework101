from lib2to3.pgen2 import driver
from time import sleep
from configs import cliente
from selenium.webdriver.common.by import By
from controladores import log_controller


class PantallaPrincipal():
    
    # Se obtienen el driver disponible
    driver = cliente.obtener_driver()

    #Elementos de la pagina
    dropdown_rol = "//select[@id='roles']"
    btn_establecer_rol = "//a[@id='imgBtn0']"
    dropdown_file = "//td[@id='mFile']"
    btn_new_inc = "//a[@id='toolbar_0']"
    txt_Cliente = "//input[@pdmqa='zorg_id']"

    def selecciona_rol(self, rol):
        sleep(3)
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
        sleep(3)

    #def crear_nuevo_incidente(self):
    #    self.driver.switch_to.frame("product")
    #    self.driver.switch_to.frame("tab_2000")
    #    self.driver.switch_to.frame("menubar")
    #    crear_nuevo_inc_element = self.driver.find_element(By.XPATH, self.dropdown_file)
    #    crear_nuevo_inc_element.click()
    #    self.driver.switch_to.default_content()
    #    self.driver.switch_to.default_content()
    #    self.driver.switch_to.default_content()
    #    self.driver.execute_script('var pressthiskey = "i";var e = new Event("keydown");e.key = pressthiskey;e.keyCode = e.key.charCodeAt(0);e.which = e.keyCode;e.altKey = false;e.ctrlKey = true;e.shiftKey = false;e.metaKey = false;e.bubbles = true;document.dispatchEvent(e);')
        #crear_nuevo_inc_element.send_keys("i")
        #self.driver.switch_to.default_content()
    #    log_controller.log_info("Se selecciono crear incidente")


    def presionar_boton_new_inc(self):
        self.driver.switch_to.frame("product")
        self.driver.switch_to.frame("tab_2000")
        self.driver.switch_to.frame("menubar")
        btn_new_incidente = self.driver.find_element(By.XPATH, self.btn_new_inc)
        btn_new_incidente.click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()

    
    def escribir_cliente_id(self, id):
        #Obtenemos la ventana actual (Principal)
        ventana_actual = self.driver.current_window_handle
        #Sacamos lista de ventanas disponibles
        lista_ventanas = self.driver.window_handles
        # Iteramos sobre la lista y comparamos si hay una ventana diferente a la actual
        for wh in lista_ventanas:
            if ventana_actual != wh:
                self.driver.switch_to.window(wh) #Cambiamos a la ventana diferente a la actual
                break
    
        self.driver.switch_to.frame("cai_main")
        txt_zorg_id = self.driver.find_element(By.XPATH, self.txt_Cliente)
        txt_zorg_id.send_keys(id)

        #Regresamos a la ventana principal
        self.driver.switch_to.window(ventana_actual)