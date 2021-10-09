import imaplib
import email
import pandas as pd


mail = imaplib.IMAP4("mail.udea.com.tr")
mail.login("akif.cavdar@udea.com.tr", "password")

mail.select()
typ, data = mail.search(None, "ALL")

date_msg = list()
from_msg = list()
for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    msg_info = email.message_from_bytes(data[0][1])

    date_msg.append(msg_info.get('date'))
    from_msg.append(msg_info.get('from'))
    print('Added: <{}:{}>'.format(msg_info.get('from'), msg_info.get('date')))

date_msg = pd.to_datetime(date_msg)
date = [str(x).split(' ')[0] for x in date_msg]

df = pd.DataFrame(data={'Date': date, 'Sender': from_msg})
print(df.head())
df.to_csv('~inbox_mail.csv', index=False)

mail.close()
mail.logout()
