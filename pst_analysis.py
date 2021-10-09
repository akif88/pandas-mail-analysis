import pandas as pd
from matplotlib import pyplot as plt

mail_data = pd.read_csv('C:\\Users\\Asus\Desktop\\mail_analysis\\index_pst_mail_2.csv')
print(mail_data.groupby('Date_Monthly').count())


plt.plot(mail_data['Date_Daily'].unique(), mail_data.groupby('Date_Daily').count(), '-o')
#plt.plot(asd, mail_data.groupby('Date_Monthly').count(), '-o')
plt.xticks(rotation=90)
plt.show()
