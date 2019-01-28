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


__author__ = 'vijayago'

"""
Funtion to Verify UCSD Home Page URL
"""
@given(u'user logged in UCSD Successfully')
def validate_ucsd_homepage(context):
    try:
        WebDriverWait(context.driver, 40).until(EC.title_is("Cisco UCS Director"))
        print("User Logged in UCSD as a Admin User")

    except:
        print("User failed to login as a Admin User .. Exit Testing")
        context.driver.close()
        context.driver.quit()

"""
Funtion to click Administration Main Menu in UCSD Home Page.
"""
@when(u'user click Administration Main Menu')
def click_adminmain_menu(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(
            configReader.fetchElementLocators("UCSADD", "adminmenu_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "adminmenu_xpath"))).click()

    except:
        print("Unable to click Admin Menu")
        context.driver.close()
        context.driver.quit()


"""
Funtion to click Physical Accounts Sub Menu in UCSD Home Page.
"""
@when(u'user click Physical Accounts Sub Menu')
def click_physical_accounts(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(
            configReader.fetchElementLocators("UCSADD", "physicalacct_submenu_xpath")))))
        context.driver.find_element_by_xpath(
            (configReader.fetchElementLocators("UCSADD", "physicalacct_submenu_xpath"))).click()

    except:
        print("Unable to click Physical Accounts Menu")
        context.driver.close()
        context.driver.quit()


"""
Funtion to click Physical Accounts Tab.
"""
@when(u'user Navigate to the Physical Accounts Tab.')
def click_physical_accounts_tab(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (
            configReader.fetchElementLocators("UCSADD", "physicalacct_tab_xpath")))))
        context.driver.find_element_by_xpath(
            (configReader.fetchElementLocators("UCSADD", "physicalacct_tab_xpath"))).click()

    except:
        print("Unable to click Physical Accounts Tab")
        context.driver.close()
        context.driver.quit()


"""
Funtion to click UCS Add Button in Physical Accounts Tab .
"""
@when(u'user Click Add Button')
def click_physical_tab_add(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(
            configReader.fetchElementLocators("UCSADD", "physicalacct_add_button_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "physicalacct_add_button_xpath"))).click()

    except:
        print("Unable to click Add Button")
        context.driver.close()
        context.driver.quit()

"""
Funtion to click UCS Submit Button in Physical Accounts Tab .
"""
@when(u'user Click ucs submit button')
def click_physical_tab_submit(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(
            configReader.fetchElementLocators("UCSADD", "physicalacct_submit_button_xpath")))))
        context.driver.find_element_by_xpath(
            (configReader.fetchElementLocators("UCSADD", "physicalacct_submit_button_xpath"))).click()

    except:
        print("Unable to click Submit Button")
        context.driver.close()
        context.driver.quit()

"""
Funtion to enter Valid UCS account name in UCS Account add page .
"""
@when(u'user enter Valid UCS account name')
def enter_ucs_accountname(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "ucs_acctname_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctname_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctname_xpath"))).send_keys("UCS-70")
    except:
        print("Unable to Enter Valid UCS Account Name")
        context.driver.close()
        context.driver.quit()


"""
Funtion to enter Valid UCS account Server Address in UCS Account add page .
"""
@when(u'user enter Valid UCS Server Address')
def enter_ucs_password(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(
            configReader.fetchElementLocators("UCSADD", "ucs_acctip_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctip_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctip_xpath"))).send_keys("172.22.233.70")
    except:
        print("Unable to Enter UCS Server Address")
        context.driver.close()
        context.driver.quit()


"""
Funtion to enter Valid UCS account username in UCS Account add page .
"""
@when(u'user enter Valid Username')
def enter_ucs_username(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "ucs_username_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_username_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_username_xpath"))).send_keys("admin")
    except:
        print("Unable to Enter UCS User Name")
        context.driver.close()
        context.driver.quit()


"""
Funtion to enter Valid UCS account Password in UCS Account add page .
"""
@when(u'user enter Valid Password')
def enter_ucs_password(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(
            configReader.fetchElementLocators("UCSADD", "ucs_ucspassword_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_ucspassword_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_ucspassword_xpath"))).send_keys("cloupia12345")
    except:
        print("Unable to Enter UCS Password")
        context.driver.close()
        context.driver.quit()


"""
Funtion to Select Transport Type in UCS Account add page .
"""
@when(u'user select Transport type')
def select_ucs_transport(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (
            configReader.fetchElementLocators("UCSADD", "ucs_transport_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_transport_xpath"))).click()

        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (
            configReader.fetchElementLocators("UCSADD", "ucs_protocol_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_protocol_xpath"))).click()

    except:
        print("Unable to Select Transport Type")
        context.driver.close()
        context.driver.quit()

"""
Funtion to Click Add Button in UCS Account add page .
"""
@when(u'user click ucs add button')
def click_ucs_add(context):
    try:
        time.sleep(10)
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (configReader.fetchElementLocators("UCSADD", "ucs_add_button")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_add_button"))).click()
        func_name = util.whoami()
        ucsd_log_attach(func_name)
        print("UCS Add button clicked")
    except:
        print("Unable to Click ADD Button")
        context.driver.close
        context.driver.quit

"""
Funtion to Validate UCS Account Addition in UCSD .
"""
@then(u'UCS Account should be added successfully')
def validate_ucs_acct_addition(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (configReader.fetchElementLocators("UCSADD", "ucs_add_success")))))
        success = (context.driver.find_element_by_xpath(configReader.fetchElementLocators("UCSADD", "ucs_add_success")).text)
        assert success == 'UCS-70'
        print("UCS Account Added successfully.")

    except AssertionError:
        print("UCS Account Addition Failed")
        func_name = util.whoami()
        ucsd_screenshot_attach_allure(context, func_name)





















