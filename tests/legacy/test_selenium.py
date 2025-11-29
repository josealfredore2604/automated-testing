import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSistemaCompleto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "http://127.0.0.1:8000"

    def test_flujo_e2e_correcto(self):
        self.driver.get(self.base_url)
        
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("admin123")
        self.driver.find_element(By.ID, "btn-login").click()

        self.wait.until(EC.title_contains("Dashboard"))
        self.assertIn("Dashboard", self.driver.title)

        task_desc = "Revisar servidores"
        self.driver.find_element(By.ID, "task_name").send_keys(task_desc)
        
        dropdown = Select(self.driver.find_element(By.ID, "priority"))
        dropdown.select_by_value("Alta")
        
        self.driver.find_element(By.ID, "btn-add").click()

        self.wait.until(EC.text_to_be_present_in_element((By.ID, "lista-tareas"), task_desc))
        
        lista_tareas = self.driver.find_element(By.ID, "lista-tareas").text
        self.assertIn(task_desc, lista_tareas)
        self.assertIn("Alta", lista_tareas)

        self.driver.find_element(By.ID, "btn-logout").click()
        
        self.wait.until(EC.title_contains("Portal Seguro"))
        self.assertIn("Portal Seguro", self.driver.title)

    def test_login_fallido(self):
        self.driver.get(self.base_url)
        
        self.driver.find_element(By.ID, "username").send_keys("usuario_falso")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "btn-login").click()

        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error")))
        
        error_msg = self.driver.find_element(By.CLASS_NAME, "error").text
        self.assertEqual(error_msg, "Credenciales Incorrectas")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()