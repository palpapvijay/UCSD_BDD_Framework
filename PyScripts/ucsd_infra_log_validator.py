import threading, paramiko
import time
import json
from utils import util as util



strdata=''
fulldata=''

class ssh:
    shell = None
    client = None
    transport = None

    def __init__(self, address, username, password):
        print("Connecting to server on ip", str(address) + ".")
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)
        self.transport = paramiko.Transport((address, 22))
        self.transport.connect(username=username, password=password)

        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def close_connection(self):
        if(self.client != None):
            self.client.close()
            self.transport.close()

    def open_shell(self):
        self.shell = self.client.invoke_shell()

    def send_shell(self, command):
        if(self.shell):
            self.shell.send(command + "\n")
        else:
            print("Shell not opened.")

    def process(self):
        global strdata, fulldata
        while True:
            # Print data when available
            if self.shell is not None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)
                strdata = strdata + str(alldata)
                fulldata = fulldata + str(alldata)
                strdata = self.print_lines(strdata) # print all received data except last line

    def print_lines(self, data):
        last_line = data
        if '\n' in data:
            lines = data.splitlines()
            for i in range(0, len(lines)-1):
                print(lines[i])
            last_line = lines[len(lines) - 1]
            if data.endswith('\n'):
                print(last_line)
                last_line = ''
        return last_line


def ucsd_log_validator(sshserver,sshusername,sshpassword):
    connection = ssh(sshserver, sshusername, sshpassword)
    connection.open_shell()
    connection.send_shell(util.cmd1)
    print("Server Connected and Navigated to log path:")
    connection.send_shell(util.cmd2)
    time.sleep(10)
    filePath = "C:/Users/vijayago/PycharmProjects/UCSD_BDD_Framework/Logs/Infra_log.txt"
    temp=open(filePath,"w")
    temp.write(strdata)
    temp.close()
    f = open(filePath,'r+')
    str1 = f.read()
    x = str1.split('\\r\\n')
    ErrorList = ["ERROR","Error","error","Exception","EXCEPTION","exception","JDOUser"] #Add list of Keyword to search in Infra logs
    flag = False
    outFile = "C:/Users/vijayago/PycharmProjects/UCSD_BDD_Framework/Logs/Error_log.txt"
    for line in x:
        for err in ErrorList:
            if (line.find(err)) > 0:
                flag = True
                with open(outFile, 'a') as f:
                    f.write(line)

    if flag == False:
        print("No Error's in the Infra log")  # if no specified keywords found in Infra log.
        return flag

    else:
        print("Found Error in Infra log , Please refer Logs/Error_log.txt file ")  # if any of the specified keyword found in the Database
        return flag

    f.close()
    connection.close_connection()






















