import matplotlib.pyplot as plt
days=["Thứ 2","Thứ3","Thứ 4","Thứ 5","Thứ 6","Thứ 7", "chủ nhật "]
temperature=[25,27,28,26,29,30,28]
plt.plot(days,temperature,"*--")
plt.title("Biểu đồ sự thay đổ của nhiệt độ trong một tuần ")
plt.ylabel("Nhiệt độ(°C)")
plt.grid(linewidth=0.3)
plt.show()