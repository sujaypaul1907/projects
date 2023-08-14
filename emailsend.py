
#Firstly - pip install secure-smtplib

#SMTP - Simple Mail Transfer Protocol library
import smtplib   

ob = smtplib.SMTP('smtp.gmail.com', 587)

#server function
ob.ehlo()  

#getting server  
ob.starttls()  

#for logging in gmail
ob.login('paulsujaykumar1997@gmail.com','lnatwgkvczmpioec') 

'''For logging in your two step verification should be on,
Step 01 : go to app password in two step verification
Step 02 : In select app choose Mail
Step 03 : In select device choose others
Step 04 : Type Website and generate
Step 05 : A 16 digit password will be generated and use it in python code as password

'''


#subject of email
subject = "Testing a mail using Python"  

#body of email
body = "Hey this is python"  

message = "subject:{}\n\n{}".format(subject, body)

#multiple receiver to whom we are sending email
listadd = ['protimapaul1975@gmail.com','paulsushilkumar@gmail.com'] 

#sending mail function with sender and recerver mail id with the message
ob.sendmail('paulsujaykumar1997@gmail.com', listadd, message) 


#for checking executed or not
print("Email sent successfully")  

#for closing serverterminating the session
ob.quit() 




