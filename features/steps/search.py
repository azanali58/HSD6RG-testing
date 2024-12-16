import utils
from behave import given, when, then
from features.pages.home_page import HomePage


@given("the user is on the home page")
def step_impl(context):
    utils.set_driver_config(context)


@when("the user enters a valid product as '{product}'")
def step_impl(context, product):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box(product)


@when("the user clicks on the search button")
def step_impl(context):
    context.search_page = context.home_page.click_on_the_search_button()


@then("the valid product '{product}' is displayed")
def step_impl(context, product):
    assert context.search_page.display_status_of_valid_product(product)



@when(u'the user enters an invalid product')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box('Dell')


@when(u'the user leaves the search box blank')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box('')


@then(u'a proper warning message is displayed')
def step_impl(context):
    assert context.search_page.display_status_of_warning_message('There is no product that matches the search criteria.')
    utils.quit_driver(context)
