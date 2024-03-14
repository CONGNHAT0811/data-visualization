import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# tạo font cho label
font = {'family': 'serif', 'color': 'blue', 'size': 12}

# đọc dữ liệu từ file csv 
url = "example/covid19.csv"
data = pd.read_csv(url)
# lọc lấy cột Date trong bảng
column_data = data['Date']

# Chuyển cột thành list để tìm index của ngày cần chọn
i = [row.strip() for row in column_data]
# láy data cho bar
row_name = '01 May'
z = i.index(row_name)
# lấy data cho plot
row_name1 = '31 March'
row_name2 = '13 May'
x = i.index(row_name1)
y = i.index(row_name2)

# lọc ra bảng csv mới với điều kiện 
filtered_data_bar = data.loc[z:z, ['Date', 'Daily Recovered', 'Daily Deceased', 'Daily Confirmed']]
filtered_data_plot = data.loc[x:y,['Date', 'Daily Recovered', 'Daily Deceased', 'Daily Confirmed']]

# lấy giá trị của các cột trong bảng filtered_data_bar
a = filtered_data_bar.iloc[0, filtered_data_bar.columns.get_loc('Daily Recovered')]
b = filtered_data_bar.iloc[0, filtered_data_bar.columns.get_loc('Daily Deceased')]
c = filtered_data_bar.iloc[0, filtered_data_bar.columns.get_loc('Daily Confirmed')]

# gán giá trị và tên cột
x_values = np.array(["Daily Recovered", "Daily Deceased", "Daily Confirmed"])
y_values = np.array([a, b, c])

# Tạo figure và các axes cho subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 7))

# Biểu đồ thứ nhất: Biểu đồ đường
axs[0].plot(filtered_data_plot['Date'], filtered_data_plot['Daily Confirmed'], "o-")
axs[0].set_facecolor('black')
axs[0].set_xlabel('Date', fontdict=font)
axs[0].set_ylabel('Number of Confirmed Cases', fontdict=font)
axs[0].tick_params( axis='x',rotation=45,)
axs[0].tick_params(which='major', labelsize=7)
axs[0].grid(linewidth=0.25)

# Biểu đồ thứ hai: Biểu đồ cột
axs[1].bar(x_values, y_values, color=['green', 'red', 'blue'], width=0.4)
axs[1].set_ylabel('Number of Cases', fontdict=font)
axs[1].tick_params(which='major', labelsize=7)
axs[1].set_xlabel("Number of cases on 01 May", fontdict=font)
plt.tight_layout()
plt.show()
