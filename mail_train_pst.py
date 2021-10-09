import win32com.client

import pandas as pd


outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the index of a folder - in this case,
                                     # the inbox. You can change that number to reference
                                     # any other folder

#inbox = outlook.Folders('a***.a***@udea.com.tr').Folders('Inbox')

messages = inbox.Items

date_msg = list()
sender_msg = list()
for message in messages:
    # print(message.senton.date())
    # print(message.subject)
    # print(message.sender)
    date_msg.append(message.senton.date())
    sender_msg.append(message.sender)
    print('Added: <{}:{}>'.format(message.senton.date(), message.sender))

monthly = [str(i).split('-')[0]+'-'+str(i).split('-')[1] for i in date_msg]
print(monthly)

df = pd.DataFrame(data={'Date_Monthly': monthly, 'Date_Daily': date_msg, 'Sender': sender_msg})
print(df.tail(10))
df.to_csv('index_pst_mail_2.csv', index=False)
