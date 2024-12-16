import utils
from behave import given, when, then
from features.pages.home_page import HomePage


@given("the user is logged in")
def step_impl(context):
    utils.set_driver_config(context)
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_option()
    context.login_page = context.home_page.click_on_login_option()
    context.login_page.enter_email('srk@srk.com')
    context.login_page.enter_password('ABCXYZ')
    context.account_page = context.login_page.click_on_login_button()


@given("the user is on the my account page")
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()


@given("the user clicks on the \'Changing your password\' option")
def step_impl(context):
    context.change_password_page = context.account_page.click_on_change_your_password_option()


@given("the user enters a new password as '{password}'")
def step_impl(context, password):
    context.change_password_page.enter_password(password)


@given("the user confirms the new password as '{c_password}'")
def step_impl(context, c_password):
    context.change_password_page.confirm_password(c_password)


@when("the user clicks on the password continue button")
def step_impl(context):
    context.change_password_page.click_on_continue_button()


@given("the user clicks on \'Edit your account information option\'")
def step_impl(context):
    context.edit_account_page = context.account_page.click_on_edit_your_account_information_option()


@when("the user clicks on the email continue button")
def step_impl(context):
    context.edit_account_page.click_on_continue_button()


@given("the user enters a new email")
def step_impl(context):
    context.edit_account_page.enter_new_email('srk@srk.com')


@given("the user enters a new email as '{email}'")
def step_impl(context, email):
    context.edit_account_page.enter_new_email(email)


@then("an error message is displayed")
def step_impl(context):
    assert context.edit_account_page.display_status_of_email_address_already_registered_text_message()


@then("a proper message is displayed")
def step_impl(context):
    assert context.account_page.display_status_of_your_account_has_been_successfully_updated_text_message()
    utils.quit_driver(context)
