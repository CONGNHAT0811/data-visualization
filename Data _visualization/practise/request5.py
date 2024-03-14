import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_layoffs = pd.read_csv('practise/layoffs.csv')

df_layoffs['date'] = pd.to_datetime(df_layoffs['date'])

# Lọc dữ liệu cho năm 2020 và 2022
value = df_layoffs[['total_laid_off', 'date']]

value['date'] = pd.to_datetime(value['date'])
# lấy dữ liệu từ cột date của năm 2020 và 2022
dataf_2020 = value[(value['date'].dt.year == 2020) & (value['date'].dt.month <= 11)]
dataf_2022 = value[(value['date'].dt.year == 2022) & (value['date'].dt.month <= 11)]
# loại bỏ các hàng có giá trị trống
df_2020=dataf_2020.dropna()
df_2022=dataf_2022.dropna()

# Tạo subplot với 2 hàng và 1 cột
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 7))

# Biểu đồ cho năm 2020
ax1.plot(df_2020['date'], df_2020['total_laid_off'], linewidth=0.7,color='blue')
# định dạng lable cột x
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b - %Y'))
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Laid Off')
ax1.set_title('Laid off trend for 2020')
ax1.tick_params(axis='x', rotation=45)
# đặt 2 cột y của 2 biểu đồ có độ dài bằng nhau 
ax1.set_ylim([0, max(df_2020['total_laid_off'].max(), df_2022['total_laid_off'].max())])

# Biểu đồ cho năm 2022
ax2.plot(df_2022['date'], df_2022['total_laid_off'], linewidth=0.7,color='red')
# định dạng lable cột x
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b - %Y'))
ax2.xaxis.set_major_locator(mdates.MonthLocator())
ax2.set_xlabel('Date')
ax2.set_ylabel('Total Laid Off')
ax2.set_title('Laid off trend for 2022')
ax2.tick_params(axis='x', rotation=45)
# đặt 2 cột y của 2 biểu đồ có độ dài bằng nhau 
ax2.set_ylim([0, max(df_2020['total_laid_off'].max(), df_2022['total_laid_off'].max())])

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()