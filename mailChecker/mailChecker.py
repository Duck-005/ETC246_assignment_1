import imaplib
import email

IMAP_SERVER = 'outlook.office365.com'
PORT = '993'
email_address = 'demoCyber235@hotmail.com'
password = 'Dr@sto990'

imap = imaplib.IMAP4_SSL(IMAP_SERVER)
imap.login(email_address, password)

imap.select("Inbox")
_, msgNos = imap.search(None, "ALL")

file = open("C:\\Users\\Raghavendra\\OneDrive\\Desktop\\CyberPresentation\\EmailData.txt", "w")

for msgNo in msgNos[0].split():
    _, data = imap.fetch(msgNo, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    file.write(f"From : {message.get('From')}\n")
    file.write(f"To : {message.get('To')}\n")
    file.write(f"Date : {message.get('Date')}\n")
    file.write(f"Subject : {message.get('Subject')}\n")

    for part in message.walk():  # walk() is a generator that gets the message bits
        if part.get_content_type() == "text/plain":
            file.write("Body : " + part.get_payload())
    file.write('\n')

print("data saved to file")
file.close()
imap.close()
