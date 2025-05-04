data['year'] = data['researchDate'].dt.year
pre_2024 = data[data['year'] < 2024]
post_2024 = data[data['year'] >= 2024]
print("\nСредний SalesRtgPer до 2024:", pre_2024['SalesRtgPer'].mean())
print("Средний SalesRtgPer с 2024:", post_2024['SalesRtgPer'].mean())

plt.figure(figsize=(8, 6))
sns.boxplot(x='year', y='SalesRtgPer', data=data)
plt.title('SalesRtgPer по годам')
plt.show()