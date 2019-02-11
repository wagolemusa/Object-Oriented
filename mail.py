import smtplib
subject = "Hello refuge"
msg = "Whats up man"
def send_email(subject, msg):

	content="hello world"
	mail=smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login("homiemusa@gmail.com", "djrefuge@12")
	message = 'Subject: {} {}'.format(subject, msg)
	mail.sendmail("subject", "msg")
	mail.close()

# subject = "Hello refuge"
# msg = "Whats up man"
send_email("subject", "msg")