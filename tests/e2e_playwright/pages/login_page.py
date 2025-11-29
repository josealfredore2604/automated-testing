class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username_input = page.locator("#username")
        self._password_input = page.locator("#password")
        self._login_button = page.locator("#btn-login")
        self._error_message = page.locator(".error")

    def navigate(self):
        self.page.goto("http://127.0.0.1:8000")

    def login(self, username, password):
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()

    def get_error_message(self):
        return self._error_message.inner_text()