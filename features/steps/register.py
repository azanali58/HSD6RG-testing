import utils
from behave import given, when, then
from features.pages.home_page import HomePage


@given(u'the user is on the registration page')
def step_impl(context):
    utils.set_driver_config(context)
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_option()
    context.register_page = context.home_page.click_on_register_option()


@when("the user enters the firstname as '{fname}'")
def step_impl(context, fname):
    fname = '' if fname == '[blank]' else fname
    context.register_page.enter_first_name(fname)


@when("the user enters the lastname as '{lname}'")
def step_impl(context,lname):
    lname = '' if lname == '[blank]' else lname
    context.register_page.enter_last_name(lname)


@when("the user enters the registration email as '{email}'")
def step_impl(context, email):
    email = '' if email == '[blank]' else email
    context.register_page.enter_email(email)


@when("the user enters the telephone number as '{t_no}'")
def step_impl(context,t_no):
    t_no = '' if t_no == '[blank]' else t_no
    context.register_page.enter_telephone(t_no)


@when("the user enters the registration password as '{password}'")
def step_impl(context, password):
    password = '' if password == '[blank]' else password
    context.register_page.enter_password(password)
    context.register_page.confirm_password(password)


@when('the user checks the privacy policy option')
def step_impl(context):
    context.register_page.check_privacy_policy_option()


@when('the user clicks on the continue button')
def step_impl(context):
    context.account_created_page = context.register_page.click_on_continue_button()


@then("the user is registered")
def step_impl(context):
    assert context.account_created_page.display_status_of_your_account_has_been_created_header('Your Account Has Been Created!')



@then(u'a \'Warning: E-Mail Address is already registered!\' is displayed')
def step_impl(context):
    assert context.register_page.display_status_of_email_address_already_registered_text_message('Warning: E-Mail Address is already registered!')



@then(u'a \'Telephone must be between 3 and 32 characters!\' is displayed')
def step_impl(context):
    assert context.register_page.display_status_of_telephone_number_must_be_between_3_and_32_characters_text_message('Telephone must be between 3 and 32 characters!')





@then(u'a \'Password must be between 4 and 20 characters!\' is displayed')
def step_impl(context):
    assert context.register_page.display_status_of_password_must_be_between_4_and_20_characters_text_message('Password must be between 4 and 20 characters!')






