import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_parth='practise/layoffs.csv'
df=pd.read_csv(file_parth)
value = df[['industry', 'total_laid_off']]
industry_sum = value.groupby('industry').sum()
sorted_industry_sum = industry_sum.sort_values(by='total_laid_off', ascending=False)
top_5_industry = sorted_industry_sum.head(5)
myexplode = [0.2, 0, 0, 0,0]
# Vẽ biểu đồ tròn
plt.figure(figsize=(8, 8))
plt.pie(top_5_industry['total_laid_off'], labels=top_5_industry.index,explode=myexplode,shadow=True, autopct='%1.1f%%',)
plt.axis('equal')  # Đảm bảo hình tròn
plt.title('Top 5 Locations with Highest Layoffs')
plt.legend(loc='center left', bbox_to_anchor=(0.8, 0.5))
plt.show()