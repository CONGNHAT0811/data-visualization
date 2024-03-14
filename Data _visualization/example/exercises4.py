import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# tạo font cho labe
font = {'family': 'serif', 'color': 'blue', 'size': 15}
# đọc dữ liệu từ file csv 
url = "example/covid19.csv"
data = pd.read_csv(url)
# lọc lất cột Date trong bảng
column_data = data['Date']
# Chuyển cột thành list đề tìm index  của ngày cần trọn
i = [row.strip() for row in column_data]
row_name='01 May'
x=i.index(row_name )
# lọc ra bảng csv mới với điều kiện 
filtered_data = data.loc[x:x, ['Date', 'Daily Recovered', 'Daily Deceased', 'Daily Confirmed']]
# lấy giá trị của các cột trong bảng filtered_data
a = filtered_data.iloc[0, filtered_data.columns.get_loc('Daily Recovered')]
b = filtered_data.iloc[0, filtered_data.columns.get_loc('Daily Deceased')]
c = filtered_data.iloc[0, filtered_data.columns.get_loc('Daily Confirmed')]
# gán giá trị và tên cột
x = np.array(["Daily Recovered", "Daily Deceased", "Daily Confirmed"])
y = np.array([a, b, c])
# vẽ biểu đồ cột 
plt.bar(x, y, color=[ 'green', 'red','blue'], width=0.4)
plt.legend(x)
plt.xticks(rotation=360)
plt.title("Number of cases 01 May", fontdict=font)
plt.ylabel('Number of Cases', fontdict=font) 
plt.show()
