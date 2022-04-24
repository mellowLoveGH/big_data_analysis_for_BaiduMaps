#!/usr/bin/env python
#coding=utf-8
 
 
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
 
class mailmsg(object):
    def __init__(self, sender, receiver, subject, content,attach_files=None):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content
        self.attach_files = attach_files
 
    def send_email(self, attach_charset="UTF-8"):
        """
        鍙戦??侀偖浠舵帴鍙??
        """
        # 鍙傛暟棰勫??勭悊
        if self.sender is None:
            print("sender is none")
        # 鏋勯??犻偖浠??
        msg = MIMEMultipart("related")
        msg["Subject"] = Header(self.subject, "UTF-8")
        msg["From"] = "<%s>" % self.sender
        receiver_list = self.receiver.split(";")
        receiver_to_list = receiver_list[0].split(",")
        if len(receiver_list) > 1:
            receiver_cc_list = receiver_list[1].split(",")
        else:
            receiver_cc_list = []
        #msg["To"] = Header(";".join(receiver_to_list), "UTF-8")
        #msg["Cc"] = Header(";".join(receiver_cc_list), "UTF-8")
        msg["To"] = ";".join(receiver_to_list)
        msg["Cc"] = ";".join(receiver_cc_list)
 
        # 鍔犲叆姝ｆ枃
        msg.attach(MIMEText(self.content, _subtype = "html", _charset="UTF-8"))
        # 鍔犲叆闄勪欢
        if self.attach_files is not None:
            for file in self.attach_files:
                part = MIMEBase("application", "octet-stream")
                file_content = ""
                infile = open(file, "rb")
                try:
                    file_content = infile.read()
                finally:
                    infile.close()
                part.set_payload(file_content, attach_charset)
                part.add_header("Content-Disposition", "attachment; filename=%s" % os.path.basename(file))
                msg.attach(part)
        # 鍙戦??侀偖浠??
        smtp = smtplib.SMTP()
        #smtp.connect("hotswap-in.baidu.com")
        smtp.connect("proxy-in.baidu.com")
        try:
            smtp.sendmail(self.sender, receiver_to_list + receiver_cc_list, msg.as_string())
        #except Exception as e:
        #    print("鍙戦??侀偖浠跺け璐??:%s" % (e))
        finally:
            #print("鍙戦??乫inally")
            smtp.quit()
 
 
if __name__ == "__main__":
    # send_email("mail_address_of_sender", "mail_address_of_receiver", "Email Test", "my content")
    report_file = open("testing04.txt","r")
    lns = report_file.readlines()
    report_content = ""
    for ln in lns[1:]:

        if "'30m'" in ln:
            report_content = report_content + "------ accuracy ------" + "<br/>"
        elif "'2km'" in ln:
            report_content = report_content + "------ badcase ------" + "<br/>"
        report_content = report_content + ln + "<br/>"
    #
    report_content = lns[0] + "<br/><pre>" + report_content + "</pre>"
    receivers = "guihan@baidu.com;liumin02@baidu.com;1341826597@qq.com"
    receivers = "guihan@baidu.com;1341826597@qq.com"
    send_baidu_mail = mailmsg("guihan@baidu.com", receivers, "log report", report_content)
    send_baidu_mail.send_email()
