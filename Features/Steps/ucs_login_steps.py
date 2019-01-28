from Lib import configReader
from utils import util as util
from PyScripts import ucsd_infra_log_validator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import moment
from Features.CommonFuncs.ucsd_common_func import *


__author__ = 'vijayago'

"""
Funtion to Verify UCSD Login Page URL
"""
@given(u'user is in UCSD Login Page')
def ucsd_login(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.title_is("Login"))
        print("UCSD Login Page Loaded Successfully")

    except:
        print("Unable to Load UCSD Login Page .. Exit Testing")
        context.driver.close()
        context.driver.quit()


"""
Funtion to Enter Valid Username in UCSD Login Page
"""
@when(u'user enters valid UCSD username')
def enter_valid_ucsd_username(context):
    context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "username_id")).send_keys("admin")

"""
Funtion to Enter Valid Password in UCSD Login Page
"""
@when(u'user enters valid UCSD password')
def enter_ucsd_password(context):
    context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "password_id")).send_keys("admin")

"""
Funtion to Click Submit Button in UCSD Login Page
"""
@when(u'user click submit button')
def click_ucsd_login_submit(context):
    try:
        context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "submit_id")).click()
        func_name = util.whoami()
        ucsd_log_attach(func_name)

    except:
        print("Unable to Click Submit Button.. Exit Testing")
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)

"""
Funtion to Validate UCSD Login Success
"""
@then(u'user should be logged in successfully')
def ucsd_login_success(context):
    try:
        element = WebDriverWait(context.driver, 40).until(EC.title_is("Cisco UCS Director"))
        assert context.driver.title == "Cisco UCS Director"

    except AssertionError:
        print("UCSD Login Failed.. Exit Testing")
        raise
        context.driver.close
        context.driver.quit

"""
Funtion to Enter Invalid Username in UCSD Login Page
"""
@when(u'user enters Invalid UCSD username')
def enter_invalid_ucsd_username(context):
    context.driver.find_element_by_id(configReader.fetchElementLocators("Login", "username_id")).send_keys("admin1")


"""
Funtion to Validate Authentication Error Message in UCSD Login Page
"""
@then(u'UCSD should provide valid error message.')
def ucsd_login_failure(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.presence_of_element_located((By.XPATH,(configReader.fetchElementLocators("Login", "Auth_Error")))))
        Err = (context.driver.find_element_by_xpath(configReader.fetchElementLocators("Login", "Auth_Error")).text)
        assert Err == "Authentication failed"
        print("Proper Error Message displayed")

    except AssertionError:
        print("Proper Error Mesage Not displayed")
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)


