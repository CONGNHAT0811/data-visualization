import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'layoffs.csv'
df_layoffs = pd.read_csv(file_path)

company_value = df_layoffs[['company', 'total_laid_off']]
company_sum = company_value.groupby('company').sum()
sorted_company_sum = company_sum.sort_values(by='total_laid_off', ascending=False)
top_10_companies = sorted_company_sum.head(10)

plt.figure(figsize=(10, 6))
bars = plt.bar(top_10_companies.index, top_10_companies['total_laid_off'], color='blue', width=0.5)

plt.xticks(rotation=45, ha='right')

# Đặt giá trị trên mỗi cột
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center')

plt.tight_layout()
plt.show()
