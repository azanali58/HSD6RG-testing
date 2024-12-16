import utils
from behave import given, when, then
from features.pages.home_page import HomePage


@given(u'the user is on the login page')
def step_impl(context):
    utils.set_driver_config(context)
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_option()
    context.login_page = context.home_page.click_on_login_option()



@when("the email field is filled with '{email}'")
def step_impl(context, email):
    email = '' if email == '[blank]' else email
    context.login_page.enter_email(email)


@when("the Password field is filled with '{password}'")
def step_impl(context, password):
    password = '' if password == '[blank]' else password
    context.login_page.enter_password(password)


@when(u'the user clicks on the login button')
def step_impl(context):
    context.account_page = context.login_page.click_on_login_button()


@then(u'the user is logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()




@then(u'a \'Warning: No match for E-Mail Address and/or Password.\' is displayed')
def step_impl(context):
    assert context.login_page.display_status_of_warning_message('Warning: No match for E-Mail Address and/or Password.')
    utils.quit_driver(context)





