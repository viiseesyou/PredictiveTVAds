missing_values = data.isnull().sum()
print("\nСтолбцы с пропущенными значениями:")
print(missing_values[missing_values > 0])

missing_percentage = (data.isnull().sum() / len(data)) * 100
missing_percentage = missing_percentage[missing_percentage > 0]
plt.figure(figsize=(10, 6))
missing_percentage.plot(kind='bar')
plt.title('Процент пропущенных значений по столбцам')
plt.ylabel('Процент')
plt.show()

Q1 = data['SalesRtgPer'].quantile(0.25)
Q3 = data['SalesRtgPer'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(data['SalesRtgPer'] < lower_bound) | (data['SalesRtgPer'] > upper_bound)]
print(f"Количество выбросов в SalesRtgPer: {len(outliers)}")