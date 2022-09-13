from configs import cliente
from selenium.webdriver.common.by import By
from controladores import log_controller


class Autenticacion():
    
    # Se obtienen el driver disponible
    driver = cliente.obtener_driver()

    #Elementos de la pagina
    txtbox_usuario = "//input[@id='USERNAME']"
    txtbox_psw = "//input[@id='PIN']"
    btn_login = "//a[@id='imgBtn0']"
    btn_guestacc = "//span[@class='guest_msg']"

    def escribir_usuario(self, user_id):
        txt_usuario = self.driver.find_element(By.XPATH, self.txtbox_usuario)
        txt_usuario.send_keys(user_id)

        log_controller.log_info(f"Se inserto el user id -> {user_id}")

    def presionar_boton_login(self):
        btn_login_elements = self.driver.find_element(By.XPATH, self.btn_login)
        btn_login_elements.click()

        log_controller.log_info("Se dio click en el boton login")