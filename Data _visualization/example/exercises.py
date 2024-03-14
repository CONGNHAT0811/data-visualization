import matplotlib.pyplot as plt
import pandas as pd
# tạo font cho label
font={'family':'serif','color':'blue','size':15}
# đọc dữ liệu từ file csv 
url = "example/covid19.csv"
data = pd.read_csv(url)
# Chuyển cột thành danh sách
column_data = data['Date']
# Chuyển cột thành danh sách
i = [row.strip() for row in column_data]
row_name1='31 March'
row_name2='13 May'
x=i.index(row_name1 )
y=i.index(row_name2 )
# lọc ra bảng csv mới với điều kiện 
filtered_data = data.loc[x:y,['Date', 'Daily Recovered', 'Daily Deceased', 'Daily Confirmed']]
# vẽ biểu đồ đường
fig,ax = plt.subplots(figsize=(12, 5))
ax.set_facecolor('black')
plt.plot(filtered_data['Date'], filtered_data['Daily Confirmed'],"o-" )
plt.xlabel('DATE',fontdict=font)
plt.ylabel('NUMBER OF CONFIRMED CASES',fontdict=font)
plt.xticks(rotation=45)
plt.tick_params( which='major', labelsize=7)
plt.grid(linewidth = 0.25)
plt.show()
