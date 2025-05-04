print("Информация о данных:")
print(data.info())
print("\nПервые 5 строк данных:")
print(data.head())

data['researchDate'] = pd.to_datetime(data['researchDate'])

print("\nПроверка breaksStartTime:")
print(data['breaksStartTime'].head())
print("Тип данных breaksStartTime:", data['breaksStartTime'].dtype)

try:

    dt_series = pd.to_datetime(data['breaksStartTime'], format='%H:%M:%S', errors='coerce')

    data['hour'] = dt_series.dt.hour
    data['minute'] = dt_series.dt.minute
    data['second'] = dt_series.dt.second

    print("Успешно созданы столбцы с временными компонентами:")
    print(data[['breaksStartTime', 'hour', 'minute', 'second']].head())

except ValueError as e:
    print(f"Ошибка при преобразовании breaksStartTime: {e}")
    problematic_rows = data[~data['breaksStartTime'].str.match(r'^\d{2}:\d{2}:\d{2}$', na=False)]
    print("Проблемные строки в breaksStartTime:")
    print(problematic_rows[['breaksStartTime']])

try:
    dt_series = pd.to_datetime(data['researchDate'], format='%Y-%m-%d', errors='coerce')

    data['day'] = dt_series.dt.day
    data['month'] = dt_series.dt.month

    print("\nУспешно созданы столбцы с датой:")
    print(data[['researchDate', 'day', 'month']].head())

except ValueError as e:
    print(f"Ошибка при преобразовании researchDate: {e}")
    problematic_rows = data[~data['researchDate'].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False)]
    print("Проблемные строки в researchDate:")
    print(problematic_rows[['researchDate']])