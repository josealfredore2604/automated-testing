import pytest
from playwright.sync_api import Page
from tests.e2e_playwright.pages.login_page import LoginPage
from tests.e2e_playwright.pages.dashboard_page import DashboardPage

def test_flujo_completo_con_pom(page: Page):
    # 1. Inicializar los objetos de página (Page Objects)
    login_p = LoginPage(page)
    dashboard_p = DashboardPage(page)

    # 2. Paso a paso legible
    login_p.navigate()
    login_p.login("admin", "admin123")

    # 3. Acciones en el dashboard
    dashboard_p.create_task("Aprender POM Avanzado", "Alta")
    
    # 4. Verificaciones
    assert dashboard_p.is_task_visible("Aprender POM Avanzado")

    # 5. Salida
    dashboard_p.logout()

def test_login_fallido(page: Page):
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("hacker", "12345")
    
    assert "Credenciales Incorrectas" in login_p.get_error_message()