import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

df = pd.read_excel('lab_4_part_5.xlsx', sheet_name='Данные', header=0)

print("Реальные названия столбцов после загрузки:")
print(df.columns.tolist())

df = df.drop(columns=['Unnamed: 0'])

new_columns = df.iloc[0].values
df.columns = new_columns

df = df.iloc[1:].reset_index(drop=True)

print(f"Данные после обработки заголовков:")
print(df.head())
print(f"Размер датасета: {df.shape}")

df['Количество'] = pd.to_numeric(df['Количество'], errors='coerce')
df['Продажи'] = pd.to_numeric(df['Продажи'], errors='coerce')
df['Себестоимость'] = pd.to_numeric(df['Себестоимость'], errors='coerce')
df['Год'] = pd.to_numeric(df['Год'], errors='coerce')
df['Год-мес'] = pd.to_numeric(df['Год-мес'], errors='coerce')

df['Дата'] = pd.to_datetime(df['Дата'], errors='coerce')

initial_count = len(df)
df = df.dropna(subset=['Количество', 'Продажи', 'Себестоимость', 'Дата'])
final_count = len(df)
print(f"Удалено строк с пропущенными значениями: {initial_count - final_count}")

print("=== ИНФОРМАЦИЯ О ДАННЫХ ===")
print(f"Размер датасета: {df.shape}")
print("Основные статистики числовых показателей:")
print(df[['Количество', 'Продажи', 'Себестоимость']].describe())

df['Прибыль'] = df['Продажи'] - df['Себестоимость']
df['Рентабельность'] = (df['Прибыль'] / df['Себестоимость']) * 100
df['Средняя_цена'] = df['Продажи'] / df['Количество']

df['Год-мес_период'] = df['Дата'].dt.to_period('M')

print("=== АНАЛИЗ ПО ТОВАРАМ ===")
product_stats = df.groupby('товар').agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum',
    'Прибыль': 'sum',
    'Средняя_цена': 'mean'
}).round(2)

product_stats['Рентабельность_%'] = (product_stats['Прибыль'] / product_stats['Себестоимость']) * 100
print("Топ-10 товаров по объему продаж:")
print(product_stats.nlargest(10, 'Продажи')[['Продажи', 'Количество', 'Рентабельность_%']])

plt.figure(figsize=(14, 8))
top_products = product_stats.nlargest(10, 'Продажи')
sns.barplot(data=top_products.reset_index(), x='Продажи', y='товар', palette='viridis')
plt.title('ТОП-10 товаров по объему продаж', fontsize=16, fontweight='bold')
plt.xlabel('Объем продаж (руб)')
plt.ylabel('Товар')
plt.tight_layout()
plt.show()

print("=== АНАЛИЗ ПО БРЕНДАМ ===")
brand_stats = df.groupby('бренд').agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum',
    'Прибыль': 'sum'
}).round(2)

brand_stats['Доля_рынка_%'] = (brand_stats['Продажи'] / brand_stats['Продажи'].sum()) * 100
brand_stats['Рентабельность_%'] = (brand_stats['Прибыль'] / brand_stats['Себестоимость']) * 100
print("Статистика по брендам:")
print(brand_stats.sort_values('Продажи', ascending=False))

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].pie(brand_stats['Доля_рынка_%'], labels=brand_stats.index, autopct='%1.1f%%', 
           colors=sns.color_palette('Set3'))
axes[0].set_title('Доля рынка по брендам', fontsize=14, fontweight='bold')

sns.barplot(data=brand_stats.reset_index(), x='бренд', y='Рентабельность_%', ax=axes[1], palette='coolwarm')
axes[1].set_title('Рентабельность по брендам', fontsize=14, fontweight='bold')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45)
axes[1].set_ylabel('Рентабельность (%)')

plt.tight_layout()
plt.show()

print("=== ДИНАМИКА ПРОДАЖ ===")
monthly_sales = df.groupby('Год-мес_период').agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum',
    'Прибыль': 'sum'
}).reset_index()

monthly_sales['Год-мес_период'] = monthly_sales['Год-мес_период'].astype(str)

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

axes[0,0].plot(monthly_sales['Год-мес_период'], monthly_sales['Продажи'], marker='o', linewidth=2)
axes[0,0].set_title('Динамика объема продаж', fontweight='bold')
axes[0,0].set_ylabel('Продажи (руб)')
axes[0,0].tick_params(axis='x', rotation=45)

axes[0,1].plot(monthly_sales['Год-мес_период'], monthly_sales['Количество'], marker='o', linewidth=2, color='orange')
axes[0,1].set_title('Динамика количества продаж', fontweight='bold')
axes[0,1].set_ylabel('Количество')
axes[0,1].tick_params(axis='x', rotation=45)

axes[1,0].plot(monthly_sales['Год-мес_период'], monthly_sales['Прибыль'], marker='o', linewidth=2, color='green')
axes[1,0].set_title('Динамика прибыли', fontweight='bold')
axes[1,0].set_ylabel('Прибыль (руб)')
axes[1,0].tick_params(axis='x', rotation=45)

monthly_sales['Рентабельность'] = (monthly_sales['Прибыль'] / monthly_sales['Себестоимость']) * 100
axes[1,1].plot(monthly_sales['Год-мес_период'], monthly_sales['Рентабельность'], marker='o', linewidth=2, color='red')
axes[1,1].set_title('Динамика рентабельности', fontweight='bold')
axes[1,1].set_ylabel('Рентабельность (%)')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print("=== СЕЗОННОСТЬ ПРОДАЖ ===")
df['Месяц'] = df['Дата'].dt.month
monthly_pattern = df.groupby('Месяц').agg({
    'Продажи': 'mean',
    'Количество': 'mean'
}).round(2)

print("Средние показатели по месяцам:")
print(monthly_pattern)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

ax1.plot(months, monthly_pattern['Продажи'], marker='o', linewidth=2.5, color='blue', label='Средние продажи')
ax1.set_title('Сезонность продаж по месяцам - Средний объем продаж', fontsize=14, fontweight='bold')
ax1.set_ylabel('Средние продажи (руб)')
ax1.grid(True, alpha=0.3)
ax1.legend()

ax2.plot(months, monthly_pattern['Количество'], marker='s', linewidth=2.5, color='orange', label='Среднее количество')
ax2.set_title('Сезонность продаж по месяцам - Среднее количество', fontsize=14, fontweight='bold')
ax2.set_xlabel('Месяц')
ax2.set_ylabel('Среднее количество (шт)')
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()

print("=== ПРОГНОЗИРОВАНИЕ ПРОДАЖ ===")

monthly_sales_sorted = monthly_sales.sort_values('Год-мес_период')
months_num = np.arange(len(monthly_sales_sorted)).reshape(-1, 1)
sales_values = monthly_sales_sorted['Продажи'].values

if len(monthly_sales_sorted) > 1:
    model = LinearRegression()
    model.fit(months_num, sales_values)

    future_months = np.arange(len(monthly_sales_sorted), len(monthly_sales_sorted) + 6).reshape(-1, 1)
    predicted_sales = model.predict(future_months)
    
    future_periods = [f'Прогноз {i+1}' for i in range(6)]
    
    all_periods = list(monthly_sales_sorted['Год-мес_период']) + future_periods
    
    plt.figure(figsize=(14, 8))
    
    plt.plot(range(len(monthly_sales_sorted)), sales_values, 
             marker='o', linewidth=2.5, label='Фактические продажи', color='blue')
    
    plt.plot(range(len(monthly_sales_sorted), len(monthly_sales_sorted) + 6), predicted_sales, 
             marker='s', linewidth=2.5, label='Прогноз', color='red', linestyle='--')
    
    plt.axvline(x=len(monthly_sales_sorted)-0.5, color='gray', linestyle=':', alpha=0.7)
    
    plt.title('Прогноз объема продаж', fontsize=16, fontweight='bold')
    plt.xlabel('Период')
    plt.ylabel('Объем продаж (руб)')
    
    tick_positions = list(range(0, len(all_periods), max(1, len(all_periods)//8)))
    tick_labels = [all_periods[i] if i < len(all_periods) else '' for i in tick_positions]
    plt.xticks(tick_positions, tick_labels, rotation=45)
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    print(f"Прогноз продаж на следующие 6 месяцев:")
    for i, sales in enumerate(predicted_sales, 1):
        print(f"  Прогноз {i}: {sales:,.2f} руб.")
    
    print(f"\nСредний прогноз продаж на следующие 6 месяцев: {predicted_sales.mean():,.2f} руб.")
    print(f"Общий тренд: {'рост' if model.coef_[0] > 0 else 'снижение'}")
    print(f"Среднемесячное изменение: {model.coef_[0]:,.2f} руб.")
else:
    print("Недостаточно данных для построения прогноза")

print("=== АНАЛИЗ РОСТА/СПАДА ===")
monthly_sales_sorted['Рост_продаж_%'] = monthly_sales_sorted['Продажи'].pct_change() * 100
monthly_sales_sorted['Рост_прибыли_%'] = monthly_sales_sorted['Прибыль'].pct_change() * 100

print("Показатели роста/спада за последние периоды:")
print(monthly_sales_sorted[['Год-мес_период', 'Продажи', 'Прибыль', 'Рост_продаж_%', 'Рост_прибыли_%']].tail(12))

print("=== АНАЛИЗ ПО ТОЧКАМ РЕАЛИЗАЦИИ ===")
point_stats = df.groupby('точка').agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Прибыль': 'sum'
}).round(2)

print("Эффективность точек реализации:")
print(point_stats)

print("=== ВЫВОДЫ ===")
print("1. Общий объем продаж за период:", f"{df['Продажи'].sum():,.2f} руб.")
print("2. Среднемесячный объем продаж:", f"{df.groupby('Год-мес_период')['Продажи'].sum().mean():,.2f} руб.")
print("3. Самый прибыльный бренд:", brand_stats.loc[brand_stats['Прибыль'].idxmax()].name)
if not brand_stats.empty:
    print("4. Самый рентабельный бренд:", brand_stats.loc[brand_stats['Рентабельность_%'].idxmax()].name)
print("5. Общая рентабельность:", f"{(df['Прибыль'].sum() / df['Себестоимость'].sum() * 100):.2f}%")
print("6. Количество уникальных товаров:", df['товар'].nunique())
print("7. Количество уникальных брендов:", df['бренд'].nunique())
print("8. Период данных:", f"{df['Дата'].min().strftime('%Y-%m-%d')} - {df['Дата'].max().strftime('%Y-%m-%d')}")