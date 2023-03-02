
#######################################################################

# Imports

#######################################################################
from sys import *
import csv
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
from my_text import*


#######################################################################

# name  : Send_mail_pdf 
# work : connecting with smtp server.
#       login
#       create massege format and attache pdf to it 
#       sending mail

#######################################################################

def send_email_pdf(destination):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls(context=ssl.create_default_context())

    try:

        server.login("gaurav.arun.pekhale@gmail.com","11June2001")

        msg = MIMEMultipart()

        message = f'{my_Messege}\n\n\n\t-Gaurav Arun Pekhale'
        msg['Subject'] = my_Subject
        msg['From'] = 'gaurav.arun.pekhale@gmail.com'
        msg['To'] = destination

        msg.attach(MIMEText(message, "plain"))

        with open(pdf_file, "rb") as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(pdf_file))
        msg.attach(attach)

        server.send_message(msg)
    except Exception as E:
        print("Not Valid mail : ", destination)
        print('\n',E,'\n')



#######################################################################

# name  : Read_csv
# work : Read CSV file and fetch email throu it .
#         calls the Send_mail function

#######################################################################

def Read_CSV():
    
    try:
        isExist = os.path.exists('email.csv')
        if isExist:
            csvfile=open('email.csv','r',newline='')
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')    #return data  in List format

            for row  in reader:
                send_email_pdf(row[1])
        else :
            print("Invalide Path")

    except Exception as E:
        print("EXception Occured :",E)
        



#######################################################################

# name  : main 
# work : Primary Checks and Function call

#######################################################################

def main():

    print("Application name :",argv[0])
    
   
    if (len(argv)<1):
        print("Error : Invalide Number of Arguments")
        print("Please Give Flag '-u' for Usage and '-h' for Help")
        exit(0)
    if argv[1] == '-h' or argv[1] == '-H':
        print("HELP : This Script designed for Sending the Mail through python ")
        exit(0)                         
    if argv[1] == '-u' or argv[1] == '-U':
        print("Usage : Application_name password")
        exit(0)
    if argv[1] != 'Gaurav@123':
        print("Wrong Password")
        exit(0)

    
    Read_CSV()
    print("Success")
    


#######################################################################

# name  : Starter 
# work : if this is main thread then entre in block

#######################################################################

if __name__=="__main__":
    main()