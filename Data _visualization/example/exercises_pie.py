import matplotlib.pyplot as plt
import numpy as np
products=["Áo","Quần","Giày","Túi xách","Đồ hồ "]
myexplode = [0, 0, 0, 0,0.2]
sales=[250,180,150,120,90]
plt.pie(sales,labels=products,explode=myexplode,autopct='%1.2f%%',shadow=True,startangle=130)
plt.title("Phân phối của các loại sản phẩn bán được ")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.2) )
plt.show()