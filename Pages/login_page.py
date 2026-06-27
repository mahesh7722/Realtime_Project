from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "h3[data-test='error']"

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def is_login_successful(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        return True

    def is_login_failed(self):
        return self.page.is_visible(self.error_message)
