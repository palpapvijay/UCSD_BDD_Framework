import moment
from PyScripts import ucsd_infra_log_validator
import allure
from allure_commons.types import AttachmentType
from utils import util as util

def ucsd_log_attach(func_name):
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        Infrafilename = func_name + "_" + currTime
        conn = ucsd_infra_log_validator.ucsd_ssh_connector(util.sshServer, util.sshUsername, util.sshPassword)
        ucsd_infra_log_validator.ucsd_error_file(conn, Infrafilename)
        path = "C:/Users/vijayago/PycharmProjects/UCSD_BDD_Framework/Logs/" + Infrafilename + ".html"
        allure.attach(open(path, "rb").read(), name=Infrafilename, attachment_type=AttachmentType.HTML)

def ucsd_screenshot_attach_allure(context,func_name):
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        Snapshotfilename = func_name + "_" + currTime
        allure.attach(context.driver.get_screenshot_as_png(), name=Snapshotfilename, attachment_type=AttachmentType.PNG)
        print("Snapshot Attached in Allure Reports")

def ucsd_screenshot_save(context,func_name):
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        Snapshotfilename = func_name + "_" + currTime
        context.driver.save_screenshot("C:/Users/vijayago/PycharmProjects/UCSD_BDD_Framework/Screenshots/" + Snapshotfilename + ".png")
        print("Snapshot Saved in Specified Path")


