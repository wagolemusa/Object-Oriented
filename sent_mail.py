import smtplib
import config

def send_email(subject, msg):
	try:
		server = smtplib.SMTIP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS, config.PASSWARD)
		message = 'Subject: {} {}'.format(subject, msg)
		server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
		server.quit()
		print ("Success Email sent")
	except:
		print ("Email failed to send")


subject = "Testing email"
msg = "Hello how you there ?"
send_email(subject, msg)