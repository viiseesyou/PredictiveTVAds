correlation_matrix = data[['breaksDuration', 'programDuration', 'SalesRtgPer']].corr()
print("\nМатрица корреляций:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Матрица корреляций')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='breaksPrimeTimeStatusName', y='SalesRtgPer', data=data)
plt.title('SalesRtgPer по статусу прайм-тайма')
plt.show()