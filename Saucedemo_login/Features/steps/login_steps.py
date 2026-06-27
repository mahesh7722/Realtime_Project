from behave import given, when, then
from Pages.login_page import LoginPage
from utils.ai_validator import validate_result

@given("user is on the login page")
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()

@when('user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when("user clicks on login button")
def step_impl(context):
    context.login_page.click_login()

@then('user should see "{result}"')
def step_impl(context, result):
    if result.lower() == "success":
        assert context.login_page.is_login_successful(), "Login should succeed"
    elif result.lower() == "failure":
        assert context.login_page.is_login_failed(), "Login should fail"
    validate_result(result, context)
