#import smtplib
#s.login("
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("serenesherlyn@gmail.com", "password")
msg = "Hello!" 
server.sendmail("serenesherlyn@gmail.com", "serenesherlyn@gmail.com", msg)
print("success")
server.quit()
