import pandas as pd
from matplotlib import pyplot as plt

mail_data = pd.read_csv('C:\\Users\\Asus\Desktop\\mail_analysis\\~inbox_mail.csv')
print(mail_data.groupby('Sender').count())
plt.plot(mail_data['Date'].unique(), mail_data.groupby('Date').count(), '-o')
plt.show()


