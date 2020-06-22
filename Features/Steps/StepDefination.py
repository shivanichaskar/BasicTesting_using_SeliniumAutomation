from behave import *
from selenium.webdriver import Chrome

@given(u'User is on Registration page')
def step_impl(context):
    context.driver.get("http://www.theTestingWorld.com/testings")
    context.driver.maximize_window()

@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_name("fld_username").send_keys("abcd")

@when(u'User enters email')
def step_impl(context):
    context.driver.find_element_by_name("fld_email").send_keys("abcd@gmail.com")

@when(u'User enters password')
def step_impl(context):
    context.driver.find_element_by_name("fld_password").send_keys("abcd123")

@when(u'User clicks on Signup button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@type='submit' and @value='Sign up']").click()

@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")

@when(u'User enters duplicate username')
def step_impl(context):
    print("Not Registered")
