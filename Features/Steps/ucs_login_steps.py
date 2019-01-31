from Lib import configReader
from utils import util as util
from PyScripts import ucsd_infra_log_validator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import moment
from Features.CommonFuncs.ucsd_common_func import *
from Features.CommonSteps.ucsd_common_steps import *
from selenium.common.exceptions import TimeoutException

__author__ = 'vijayago'

"""
Funtion to Verify UCSD Login Page URL
"""
@given(u'user is in UCSD Login Page')
def ucsd_login(context):
    if wait_until_title(context, "Login") is True:
        print("UCSD Login Page Loaded successfully")
    else:
        print("UCSD Login page not loaded properly..Exit Testing")
        quit_browser(context)

"""
Funtion to Enter Valid Username in UCSD Login Page
"""
@when(u'user enters valid UCSD username')
def enter_valid_ucsd_username(context):
    locator = configReader.fetchElementLocators("Login", "username_id")
    Enter_Text(context,locator,"admin","ID")

"""
Funtion to Enter Valid Password in UCSD Login Page
"""
@when(u'user enters valid UCSD password')
def enter_ucsd_password(context):
    locator = configReader.fetchElementLocators("Login", "password_id")
    Enter_Text(context,locator, "admin", "ID")

"""
Funtion to Click Submit Button in UCSD Login Page
"""
@when(u'user click submit button')
def click_ucsd_login_submit(context):
    locator = configReader.fetchElementLocators("Login", "submit_id")
    if Click_Button(context,locator,"ID") is True:
        func_name = util.whoami()
        ucsd_log_attach(func_name)
    else:
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)

"""
Funtion to Validate UCSD Login Success
"""
@then(u'user should be logged in successfully')
def ucsd_login_success(context):
    if wait_until_title(context,"Cisco UCS Director") is True:
        print("User Logged In Successfully")
    else:
        print("UCSD Login Failed..Exit Testing")
        quit_browser(context)


"""
Funtion to Enter Invalid Username in UCSD Login Page
"""
@when(u'user enters Invalid UCSD username')
def enter_invalid_ucsd_username(context):
    locator = configReader.fetchElementLocators("Login", "username_id")
    Enter_Text(context,locator, "admin1", "ID")

"""
Funtion to Validate Authentication Error Message in UCSD Login Page
"""
@then(u'UCSD should provide valid error message.')
def ucsd_login_failure(context):
    locator = configReader.fetchElementLocators("Login", "Auth_Error")
    if presence_of_element(context,locator,"XPATH") is True:
        print("Proper Error Message displayed")
    else:
        print("Proper Error Message not Displayed")
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)



