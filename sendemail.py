import smtplib


sender = "takukelvin01@gmail.com"
receiver = "kevyblezer01@gmail.com"
password =  "0786682192@Tk"
subjet = "Python Email Test"
body =  "i just did that man"

message = f"""From:Takudzwa{sender}
To:Mukaro{receiver}
Subject:{subjet}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com ",587)
server.starttls()
try:
    server.login(sender,password)
    print("logged in...")
    server.sendmail(sender ,receiver,message)
    print("email has been sent!")
    
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")    
    

