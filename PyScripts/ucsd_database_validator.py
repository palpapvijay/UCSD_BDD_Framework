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
        self.client.connect(address, username=username, password=password, look_for_keys=False, timeout=10)
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


def ucsd_DB_log_validator(sshserver,sshusername,sshpassword):
    connection = ssh(sshserver, sshusername, sshpassword)
    connection.open_shell()
    connection.send_shell(util.cmd3)
    connection.send_shell(util.cmd4)
    connection.send_shell(util.cmd5)
    connection.send_shell(util.cmd6)
    print('Executing Query...Please wait')
    connection.send_shell(util.query1)
    time.sleep(10)
    temp=open("C:/Users/vijayago/PycharmProjects/UCSD_BDD_Framework/DB_Logs/dbfile.txt","w")
    temp.write(strdata)
    temp.close()
    f = open("C:/Users/vijayago/PycharmProjects/UCSD_BDD_Framework/DB_Logs/dbfile.txt",'r+')
    str1 = f.read()
    x = str1.split('\\r\\n')
    DBList = ["UCSMAccount","10.23.209.23"] #Add list of database Keyword value to check in DB.
    flag = False
    for line in x:
        for err in DBList:
            if (line.find(err)) > 0 :
                flag = True

    if flag == False:
        print("Data Not found in the Database") #if specified Keyword not found in DB.
    else:
        print("Data found in the Database ") #if Specified keyword found in DB.
    connection.close_connection()
                                    
                            
                      

