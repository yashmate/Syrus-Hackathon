import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
fromaddr = "healthyheartdoctor@gmail.com"
toaddr = '2017.akash.magdum@ves.ac.in'
msg = MIMEMultipart() 
msg['From'] = "healthyheartdoctor@gmail.com" 
msg['To'] = toaddr 
msg['Subject'] = "Daily Health Report"

body = "TAKE CARE!"
msg.attach(MIMEText(body, 'plain')) 
filename = "healthreport.pdf"
attachment = open("healthreport.pdf", "rb") 
p = MIMEBase('application', 'octet-stream')  
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "Doctorheart@123") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 
