import behave
from selenium import webdriver
from Lib import configReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'user logged in UCSD Successfully')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.title_is("Cisco UCS Director"))
        print("User Logged in UCSD as a Admin User")

    except:
        print("User failed to login as a Admin User .. Exit Testing")
        context.driver.close()
        context.driver.quit()


@when(u'user click Administration Main Menu')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "adminmenu_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "adminmenu_xpath"))).click()

    except:
        print("Unable to click Admin Menu")


@when(u'user click Physical Accounts Sub Menu')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "physicalacct_submenu_xpath")))))
        context.driver.find_element_by_xpath(
            (configReader.fetchElementLocators("UCSADD", "physicalacct_submenu_xpath"))).click()

    except:
        print("Unable to click Physical Accounts Menu")


@when(u'user Navigate to the Physical Accounts Tab.')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (configReader.fetchElementLocators("UCSADD", "physicalacct_tab_xpath")))))
        context.driver.find_element_by_xpath(
            (configReader.fetchElementLocators("UCSADD", "physicalacct_tab_xpath"))).click()

    except:
        print("Unable to click Physical Accounts Tab")


@when(u'user Click Add Button')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "physicalacct_add_button_xpath")))))
        context.driver.find_element_by_xpath(
            (configReader.fetchElementLocators("UCSADD", "physicalacct_add_button_xpath"))).click()

    except:
        print("Unable to click Add Button")


@when(u'user Click ucs submit button')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "physicalacct_submit_button_xpath")))))
        context.driver.find_element_by_xpath(
            (configReader.fetchElementLocators("UCSADD", "physicalacct_submit_button_xpath"))).click()

    except:
        print("Unable to click Submit Button")

@when(u'user enter Valid UCS account name')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "ucs_acctname_xpath") ))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctname_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctname_xpath"))).send_keys("UCSMAccount")
    except:
        print("Unable to Enter UCS Account IP")


@when(u'user enter Valid UCS Server Address')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "ucs_acctip_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctip_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_acctip_xpath"))).send_keys("10.23.209.23")
    except:
        print("Unable to Enter UCS Account IP")


@when(u'user enter Valid Username')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "ucs_username_xpath") ))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_username_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_username_xpath"))).send_keys("admin")
    except:
        print("Unable to Enter UCS User Name")


@when(u'user enter Valid Password')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH,(configReader.fetchElementLocators("UCSADD", "ucs_ucspassword_xpath") ))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_ucspassword_xpath"))).clear()
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_ucspassword_xpath"))).send_keys("Cloupia!123")
    except:
        print("Unable to Enter UCS Password")


@when(u'user select Transport type')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (configReader.fetchElementLocators("UCSADD", "ucs_transport_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_transport_xpath"))).click()

        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (configReader.fetchElementLocators("UCSADD", "ucs_protocol_xpath")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_protocol_xpath"))).click()

    except:
        print("Unable to Select Transport Type")

@when(u'user click ucs add button')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, (configReader.fetchElementLocators("UCSADD", "ucs_add_button")))))
        context.driver.find_element_by_xpath((configReader.fetchElementLocators("UCSADD", "ucs_add_button"))).click()

    except:
        print("Unable to click ucs add button")


@then(u'UCS Account should be added successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then UCS Account should be added successfully')



