import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
url = 'practise/layoffs.csv'
df_layoffs = pd.read_csv(url)
value = df_layoffs[['total_laid_off', 'date']]
value['date'] = pd.to_datetime(value['date'])
dataf_2023 = value[(value['date'].dt.year == 2023) & (value['date'].dt.month <= 11)]
df_2023=dataf_2023.dropna()
plt.figure(figsize=(10,7))
plt.plot(df_2023['date'],df_2023['total_laid_off'],linewidth='0.7')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b - %Y'))  
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  
plt.xlabel("Date")
plt.ylabel("Total Laid Off")
plt.title('Laid off trend for 2023')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
