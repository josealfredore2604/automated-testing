from playwright.sync_api import expect

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self._task_input = page.locator("#task_name")
        self._priority_select = page.locator("#priority")
        self._add_button = page.locator("#btn-add")
        self._task_list = page.locator("#lista-tareas")
        self._logout_button = page.locator("#btn-logout")

    def create_task(self, name, priority):
        self._task_input.fill(name)
        self._priority_select.select_option(priority)
        self._add_button.click()

    def is_task_visible(self, task_name):
        # Espera automática a que aparezca
        expect(self._task_list).to_contain_text(task_name)
        return True

    def logout(self):
        self._logout_button.click()