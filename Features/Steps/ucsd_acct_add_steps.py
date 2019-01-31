from Lib import configReader
from utils import util as util
from PyScripts import ucsd_infra_log_validator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import moment
import allure
from allure_commons.types import AttachmentType
from Features.CommonFuncs.ucsd_common_func import *
from Features.CommonSteps.ucsd_common_steps import *
from selenium.common.exceptions import TimeoutException


__author__ = 'vijayago'

"""
Funtion to Verify UCSD Home Page URL
"""
@given(u'user should be logged in successfully')
def ucsd_login_success(context):
    if wait_until_title(context,"Cisco UCS Director") is True:
        print("User Logged In Successfully")
    else:
        print("UCSD Login Failed..Exit Testing")
        quit_browser(context)


"""
Function to Click Administration Main Menu
"""
@when(u'user click Administration Main Menu')
def click_adminmain_menu(context):
    locator = configReader.fetchElementLocators("UCSADD", "adminmenu_xpath")
    if Click_Menu(context, locator, "XPATH") is True:
        print("Administration Main Menu Clicked")
    else:
        print("Unable to Click Administration Main Menu")


"""
Function to Click Physical Account Sub Menu
"""
@when(u'user click Physical Accounts Sub Menu')
def click_physical_accounts(context):
    locator = configReader.fetchElementLocators("UCSADD", "physicalacct_submenu_xpath")
    if Click_Menu(context, locator, "XPATH") is True:
        print("Administration Sub Main Menu Clicked")
    else:
        print("Unable to Click Administration Sub Main Menu")


"""
Function to Navigate to the Physical Accounts Tab
"""
@when(u'user Navigate to the Physical Accounts Tab.')
def click_physical_accounts_tab(context):
    locator = configReader.fetchElementLocators("UCSADD", "physicalacct_tab_xpath")
    if Click_Menu(context, locator, "XPATH") is True:
        print("Physical Account tab Clicked")
    else:
        print("Unable to Click Physical Account tab")


"""
Function to Click Physical tab Add Button
"""
@when(u'user Click Add Button')
def click_physical_tab_add(context):
    locator = configReader.fetchElementLocators("UCSADD", "physicalacct_add_button_xpath")
    if Click_Menu(context, locator, "XPATH") is True:
        print("Physical Account tab Add Button Clicked")
    else:
        print("Unable to Click Physical Account tab Add Button")


"""
Function to Click Physical tab Add Button
"""
@when(u'user Click ucs submit button')
def click_physical_tab_submit(context):
    locator = configReader.fetchElementLocators("UCSADD", "physicalacct_submit_button_xpath")
    if Click_Button(context, locator, "XPATH") is True:
        func_name = util.whoami()
        ucsd_log_attach(func_name)
    else:
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)


"""
Function to Enter UCS Account Name
"""
@when(u'user enter Valid UCS account name')
def enter_ucs_accountname(context):
    locator = configReader.fetchElementLocators("UCSADD", "ucs_acctname_xpath")
    Enter_Text(context, locator, "UCS-70", "XPATH")


"""
Function to Enter UCS Server IP Address
"""
@when(u'user enter Valid UCS Server Address')
def enter_ucs_password(context):
    locator = configReader.fetchElementLocators("UCSADD", "ucs_acctip_xpath")
    Enter_Text(context, locator, "172.22.233.70", "XPATH")


"""
Function to Enter Valid UCS User Name
"""
@when(u'user enter Valid Username')
def enter_ucs_username(context):
    locator = configReader.fetchElementLocators("UCSADD", "ucs_username_xpath")
    Enter_Text(context, locator, "admin", "XPATH")


"""
Function to Enter Valid UCS Password
"""
@when(u'user enter Valid Password')
def enter_ucs_password(context):
    locator = configReader.fetchElementLocators("UCSADD", "ucs_ucspassword_xpath")
    Enter_Text(context, locator, "cloupia12345", "XPATH")


"""
Function to Select UCS Transport and Protocol 
"""
@when(u'user select Transport type')
def select_ucs_transport(context):
    locator = configReader.fetchElementLocators("UCSADD", "ucs_transport_xpath")
    locator1 = configReader.fetchElementLocators("UCSADD", "ucs_protocol_xpath")
    if Click_Combo(context,locator,"XPATH") is True:
        print("UCS Transport Type Selected")
        if Click_Combo(context, locator1, "XPATH") is True:
            print("UCS Protocol Selected")
        else:
            print("Unable to select Protocol")
    else:
        print("Unable to select Transport Type")


"""
Function to Click Add Button in UCS Account Addition Page
"""
@when(u'user click ucs add button')
def click_ucs_add(context):
    locator = configReader.fetchElementLocators("UCSADD", "ucs_add_button")
    time.sleep(5)
    if Click_Button(context, locator, "XPATH") is True:
        func_name = util.whoami()
        ucsd_log_attach(func_name)
    else:
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)


"""
Function to Validate UCS Account addition
"""
@then(u'UCS Account should be added successfully')
def validate_ucs_acct_addition(context):
    try:
        locator = configReader.fetchElementLocators("UCSADD", "ucs_add_success")
        if presence_of_element(context, locator, "XPATH") is True:
            print("UCS Account Added successfully")
    except:
        print("UCS Account Addition Failed")
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)
        raise


















