import behave
from selenium import webdriver
from Lib import configReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'user is on UCSD Login Page')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.title_is("Login"))
        print("UCSD Login Page Loaded Successfully")

    except:
        print("Unable to Load UCSD Login Page .. Exit Testing")
        context.driver.close()
        context.driver.quit()


@when(u'user enters valid UCSD username')
def step_impl(context):
    context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "username_id")).send_keys("admin")


@when(u'user enters valid UCSD password')
def step_impl(context):
    context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "password_id")).send_keys("admin")


@when(u'user click submit button')
def step_impl(context):
    context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "submit_id")).click()


@then(u'user should be logged in successfully')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.title_is("Cisco UCS Director"))
        assert context.driver.title == "Cisco UCS Director"

    except AssertionError:
        print("UCSD Login Failed")
        raise


@when(u'user enters Invalid UCSD username')
def step_impl(context):
    context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "username_id")).send_keys("admin1")


@then(u'UCSD should provide valid error message.')
def step_impl(context):
    title1 = context.driver.title
    assert title1 == "Login"

# @given(u'Given user logged in UCSD Successfully')
# def step_impl(context):
#     try:
#         WebDriverWait(context.driver, 50).until(EC.title_is("Cisco UCS Director"))
#         assert context.driver.title == "Cisco UCS Director"
#         print("Login Success")
#
#     except AssertionError as Error:
#         print("User failed to login as a Admin User .. Exit Testing")
#         print(Error)
#         raise
#         context.driver.exit()



# @when(u'user click Administration Main Menu')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user click Administration Main Menu')
#
#
# @when(u'user click Physical Accounts Sub Menu')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user click Physical Accounts Sub Menu')
#
#
# @when(u'user Navigate to the Physical Accounts Tab.')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user Navigate to the Physical Accounts Tab.')
#
#
# @when(u'user Click Add Button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user Click Add Button')
#
#
# @when(u'user select Pod')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user select Pod')
#
#
# @when(u'user select Category as Computing')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user select Category as Computing')
#
#
# @when(u'user select Account Type as UCSM')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user select Account Type as UCSM')
#
#
# @when(u'user enter Valid UCS account name')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user enter Valid UCS account name')
#
#
# @when(u'user enter Valid UCS Server Address')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user enter Valid UCS Server Address')
#
#
# @when(u'user enter Valid Username')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user enter Valid Username')
#
#
# @when(u'user enter Valid Password')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user enter Valid Password')
#
#
# @when(u'user select port type')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user select port type')
#
#
# @when(u'user click add button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user click add button')
#
#
# @then(u'UCS Account should be added successfully')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then UCS Account should be added successfully')
#

