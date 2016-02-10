__author__ = 'Michael'


import smtplib
import urllib
import re
import ipgetter

class smtpSetup():

    def __init__(self,message,username,password,sendTo,outgoingServer,port):

        self.msg = message
        self.to = sendTo
        self.user = username
        self.pwd = password
        self.outgoingServer = outgoingServer
        self.port = port


    def sendMSG(self):
        smtpserver = smtplib.SMTP(self.outgoingServer, self.port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(self.user, self.pwd)
        header = 'To:' + self.to + '\n' + 'From: ' + self.user + '\n' + 'Subject:testing \n'

        smtpserver.sendmail(self.user, self.to, self.msg)

        smtpserver.close()

    def changeMessage(self,message):
        self.msg = message

    def switchReceiver(self,receiver):
        self.to = receiver

    def switchAccount(self,account, password):
        self.user = account
        self.pwd = password

    def printMsg(self):
        print(self.msg)

def get_external_ip():
    ip = ipgetter.myip()
    return ip

if __name__ == "__main__":

    message = get_external_ip()
    username = "mikecolistro@gmail.com"
    password =
    to = "mikecolistro@gmail.com"
    outgoingServer = "smtp.gmail.com"
    port = "587"
    text = smtpSetup(message, username, password, to, outgoingServer, port)
    text.sendMSG()