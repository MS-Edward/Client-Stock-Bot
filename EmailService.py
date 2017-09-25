import smtplib

class Email:

    username = 'MyEmail@gmail.com'
    password = '123Password'
    targetEmail = 'TargetEmail@gmail.com'
    conn = smtplib.SMTP('smtp.gmail.com', 587)

    def __init__(self, subject, message, sender):
        self.message = message
        self.subject = subject
        self.sender = sender
        self.openConnection()
        self.sendEmail()
        self.closeConnection()

    def openConnection(self):
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(self.username, self.password)

    def closeConnection(self):
        self.conn.quit()

    def sendEmail(self):
        self.conn.sendmail(self.username, self.targetEmail, 'Subject: ' + self.subject + '\n\n' + self.message + '\n\n' + self.sender)
