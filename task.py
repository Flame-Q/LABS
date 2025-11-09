import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')

df = df.dropna(subset=['ORIG_CITY_CODE', 'DEST_CITY_CODE']) 
df['FFP_FLAG'] = df['FFP_FLAG'].fillna('NO_FFP')

print("=== ОБЩИЕ СТАТИСТИКИ ===")
print("Основные статистики числовых показателей:")
print(df.describe())
print("Информация о типах данных:")
print(df.info())
print("Количество пропущенных значений:")
print(df.isnull().sum())

print("ТОП-10 АЭРОПОРТОВ ПО ПАССАЖИРОПОТОКУ")
top_airports = pd.concat([df['ORIG_CITY_CODE'], df['DEST_CITY_CODE']]).value_counts().head(10)
print(top_airports)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_airports.index, y=top_airports.values, palette="viridis")
plt.title('Топ-10 аэропортов по пассажиропотоку', fontsize=14, fontweight='bold')
plt.xlabel('Коды аэропортов')
plt.ylabel('Количество пассажиров')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['FLIGHT_MONTH'] = pd.to_datetime(df['FLIGHT_DATE_LOC']).dt.month
monthly_traffic = df.groupby('FLIGHT_MONTH').size()

plt.figure(figsize=(12, 6))
sns.lineplot(x=monthly_traffic.index, y=monthly_traffic.values, marker='o', linewidth=2.5)
plt.title('Сезонность перелетов по месяцам', fontsize=14, fontweight='bold')
plt.xlabel('Месяц')
plt.ylabel('Количество перелетов')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

df['FLIGHT_DAY_OF_WEEK'] = pd.to_datetime(df['FLIGHT_DATE_LOC']).dt.day_name()
daily_traffic = df.groupby('FLIGHT_DAY_OF_WEEK').size()

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_traffic = daily_traffic.reindex(days_order)

plt.figure(figsize=(12, 6))
sns.barplot(x=daily_traffic.index, y=daily_traffic.values, palette="coolwarm")
plt.title('Распределение перелетов по дням недели', fontsize=14, fontweight='bold')
plt.xlabel('День недели')
plt.ylabel('Количество перелетов')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("СТАТИСТИКА ПО ТИПАМ ПАССАЖИРОВ")
pax_stats = df['PAX_TYPE'].value_counts()
print(pax_stats)

plt.figure(figsize=(10, 8))
plt.pie(pax_stats.values, labels=pax_stats.index, autopct='%1.1f%%', 
        colors=sns.color_palette('pastel'), startangle=90)
plt.title('Распределение типов пассажиров', fontsize=14, fontweight='bold')
plt.show()

revenue_by_pax = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].mean()

plt.figure(figsize=(12, 6))
sns.barplot(x=revenue_by_pax.index, y=revenue_by_pax.values, palette="rocket")
plt.title('Средний доход по типам пассажиров', fontsize=14, fontweight='bold')
plt.xlabel('Тип пассажира')
plt.ylabel('Средний доход')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

revenue_median_by_pax = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].median()

plt.figure(figsize=(12, 6))
sns.barplot(x=revenue_median_by_pax.index, y=revenue_median_by_pax.values, palette="Set3")
plt.title('Медианный доход по типам пассажиров', fontsize=14, fontweight='bold')
plt.xlabel('Тип пассажира')
plt.ylabel('Медианный доход')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("СПОСОБЫ ОПЛАТЫ")
payment_stats = df['FOP_TYPE_CODE'].value_counts().head(10)
print(payment_stats)

plt.figure(figsize=(12, 6))
sns.barplot(x=payment_stats.index, y=payment_stats.values, palette="magma")
plt.title('Топ-10 способов оплаты', fontsize=14, fontweight='bold')
plt.xlabel('Тип оплаты')
plt.ylabel('Количество транзакций')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

revenue_by_payment = df.groupby('FOP_TYPE_CODE')['REVENUE_AMOUNT'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=revenue_by_payment.index, y=revenue_by_payment.values, palette="plasma")
plt.title('Средний доход по способам оплаты (топ-10)', fontsize=14, fontweight='bold')
plt.xlabel('Тип оплаты')
plt.ylabel('Средний доход')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("ТИПЫ МАРШРУТОВ")
route_stats = df['ROUTE_FLIGHT_TYPE'].value_counts()
print(route_stats)

plt.figure(figsize=(10, 6))
sns.barplot(x=route_stats.index, y=route_stats.values, palette="viridis")
plt.title('Распределение по типам маршрутов', fontsize=14, fontweight='bold')
plt.xlabel('Тип маршрута')
plt.ylabel('Количество перелетов')
plt.tight_layout()
plt.show()

print("ПРОГРАММА ЛОЯЛЬНОСТИ")
ffp_stats = df['FFP_FLAG'].value_counts()
print(ffp_stats)

plt.figure(figsize=(8, 8))
plt.pie(ffp_stats.values, labels=ffp_stats.index, autopct='%1.1f%%', 
        colors=sns.color_palette('Set2'), startangle=90)
plt.title('Участие в программе лояльности', fontsize=14, fontweight='bold')
plt.show()

revenue_median_by_ffp = df.groupby('FFP_FLAG')['REVENUE_AMOUNT'].median()

plt.figure(figsize=(10, 6))
sns.barplot(x=revenue_median_by_ffp.index, y=revenue_median_by_ffp.values, palette="pastel")
plt.title('Медианный доход по программе лояльности', fontsize=14, fontweight='bold')
plt.xlabel('Участие в программе лояльности')
plt.ylabel('Медианный доход')
plt.tight_layout()
plt.show()

print("КАНАЛЫ ПРОДАЖ")
sale_stats = df['SALE_TYPE'].value_counts()
print(sale_stats)

plt.figure(figsize=(10, 8))
plt.pie(sale_stats.values, labels=sale_stats.index, autopct='%1.1f%%', 
        colors=sns.color_palette('tab10'), startangle=90)
plt.title('Распределение по каналам продаж', fontsize=14, fontweight='bold')
plt.show()

print("ПРОГНОЗИРОВАНИЕ ПРОДАЖ")

df['ISSUE_MONTH'] = pd.to_datetime(df['ISSUE_DATE']).dt.to_period('M')
monthly_sales = df.groupby('ISSUE_MONTH').size()

months = np.arange(len(monthly_sales)).reshape(-1, 1)
sales = monthly_sales.values

model = LinearRegression()
model.fit(months, sales)
future_months = np.arange(len(monthly_sales) + 3).reshape(-1, 1)
predicted_sales = model.predict(future_months)

plt.figure(figsize=(12, 6))
sns.lineplot(x=months.flatten(), y=sales, label='Фактические продажи', linewidth=2.5)
sns.lineplot(x=future_months.flatten(), y=predicted_sales, label='Прогноз', linewidth=2.5, linestyle='--')
plt.title('Прогноз объемов продаж билетов', fontsize=14, fontweight='bold')
plt.xlabel('Период (месяцы)')
plt.ylabel('Количество продаж')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()