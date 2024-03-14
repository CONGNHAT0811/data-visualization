import matplotlib.pyplot as plt
shop=["Cửa hàng A","Của hàng B","Cửa hàng C","Của hàng D","Cửa hàng E"]
amount=[150,180,200,220,190]
plt.bar(shop,amount)
plt.title("Biểu đồ so sánh số lượng sản phẩm bán được giữ các của hàng  ")
plt.ylabel("Số lượng sản phẩm bán được  " )
plt.xlabel("Cửa hàng ")
plt.xticks(rotation=45)
plt.grid(linewidth=0.3)
plt.show()
