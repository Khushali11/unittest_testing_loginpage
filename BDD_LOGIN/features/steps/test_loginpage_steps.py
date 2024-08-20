from behave import given, when, then
from test_loginpage import Loginpage


@given('I have a login page with valid credentials')
def step_given_login_page_with_valid_credentials(context):
    context.login_page = Loginpage("validuser", "validpassword")


@when('I log in with the username "{username}" and the password "{password}"')
def step_when_login(context, username, password):
    context.result = context.login_page.login(username, password)


@when('I validate the username "{username}"')
def step_when_validate_username(context, username):
    context.result = context.login_page.validate_username(username)


@when('I validate the password "{password}"')
def step_when_validate_password(context, password):
    context.result = context.login_page.validate_password(password)


@then('I should see "{expected_result}"')
def step_then_check_result(context, expected_result):
    assert context.result == expected_result, f"Expected '{expected_result}', but got '{context.result}'"
