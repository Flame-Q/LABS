#сгенирировать: название модели автомобиля (марка), объём, страна, кол-во л.с., цвет, год выпуска. Посчитать (дополнительный столбец) столбец кол-во лет с момента выпсука и посторить всякую визуализацию диаграммы должны быть разными
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from faker import Faker

fake = Faker('ru_RU')  

brand_country_dict = {
    'Toyota': 'Япония',
    'Honda': 'Япония',
    'Nissan': 'Япония',
    'Mazda': 'Япония',
    'Subaru': 'Япония',
    
    'BMW': 'Германия',
    'Mercedes': 'Германия',
    'Audi': 'Германия',
    'Volkswagen': 'Германия',
    'Opel': 'Германия',
    
    'Hyundai': 'Южная Корея',
    'Kia': 'Южная Корея',
    'Daewoo': 'Южная Корея',
    'SsangYong': 'Южная Корея',
    
    'Ford': 'США',
    'Chevrolet': 'США',
    'Jeep': 'США',
    'Tesla': 'США',
    'Dodge': 'США',
    
    'Renault': 'Франция',
    'Peugeot': 'Франция',
    'Citroen': 'Франция',
    
    'Fiat': 'Италия',
    'Alfa Romeo': 'Италия',
    'Ferrari': 'Италия'
}

n_rows = 100

brands = []
countries = []
volumes = []
horse_powers = []
colors = []
years = []

colors_list = ['Красный', 'Синий', 'Черный', 'Белый', 'Серый', 'Зеленый', 
               'Серебристый', 'Желтый', 'Оранжевый', 'Фиолетовый', 'Бордовый',
               'Коричневый', 'Бежевый', 'Голубой', 'Розовый']

for _ in range(n_rows):
    brand = fake.random_element(elements=list(brand_country_dict.keys()))
    brands.append(brand)
    
    countries.append(brand_country_dict[brand])
    
    volume = fake.random_int(min=1000, max=5000) / 1000.0
    volumes.append(round(volume, 1))
    
    hp = fake.random_int(min=80, max=500)
    horse_powers.append(hp)
    
    colors.append(fake.random_element(elements=colors_list))
    
    year = fake.random_int(min=1995, max=2024)
    years.append(year)

data = {
    'Марка': brands,
    'Страна': countries,
    'Объем_двигателя': volumes,
    'Лошадиные_силы': horse_powers,
    'Цвет': colors,
    'Год_выпуска': years
}

df = pd.DataFrame(data)

current_year = datetime.now().year
df['Лет_с_выпуска'] = current_year - df['Год_выпуска']

df['Возраст_категория'] = pd.cut(df['Лет_с_выпуска'], 
                                 bins=[0, 3, 7, 15, 100], 
                                 labels=['Новый (0-3 года)', 'Средний (4-7 лет)', 'Старый (8-15 лет)', 'Очень старый (15+ лет)'])

print("Первые 15 строк данных:")
print(df.head(15))
print("\n" + "="*80)

print("\nСтатистика по данным:")
print(f"Всего записей: {len(df)}")
print(f"Уникальных марок: {df['Марка'].nunique()}")
print(f"Уникальных стран: {df['Страна'].nunique()}")
print(f"Диапазон годов выпуска: {df['Год_выпуска'].min()} - {df['Год_выпуска'].max()}")
print(f"Средний возраст автомобилей: {df['Лет_с_выпуска'].mean():.1f} лет")

country_counts = df['Страна'].value_counts()
plt.pie(country_counts.values, labels=country_counts.index, autopct='%1.1f%%')
plt.title('Распределение автомобилей по странам производства', fontsize=16, fontweight='bold')
plt.show()

brand_counts = df['Марка'].value_counts().head(10)
bars = plt.bar(brand_counts.index, brand_counts.values, color='blue')
plt.title('Топ-10 самых распространенных марок автомобилей', fontsize=16, fontweight='bold')
plt.xlabel('Марка автомобиля', fontsize=12)
plt.ylabel('Количество', fontsize=12)
plt.show()

avg_hp_by_country = df.groupby('Страна')['Лошадиные_силы'].mean().sort_values(ascending=False)
bars = plt.bar(avg_hp_by_country.index, avg_hp_by_country.values, color='pink')
plt.title('Средняя мощность автомобилей по странам производства', fontsize=16, fontweight='bold')
plt.xlabel('Страна производства', fontsize=12)
plt.ylabel('Средние лошадиные силы', fontsize=12)
plt.show()

color_counts = df['Цвет'].value_counts()
plt.pie(color_counts.values, labels=color_counts.index, autopct='%1.1f%%')
plt.title('Распределение автомобилей по цветам', fontsize=16, fontweight='bold')
plt.show()

age_counts = df['Возраст_категория'].value_counts().sort_index()
bars = plt.bar(age_counts.index, age_counts.values, color='lightgreen')
plt.title('Распределение автомобилей по возрастным категориям', fontsize=16, fontweight='bold')
plt.xlabel('Возрастная категория', fontsize=12)
plt.ylabel('Количество автомобилей', fontsize=12)
plt.show()

avg_volume_by_country = df.groupby('Страна')['Объем_двигателя'].mean().sort_values(ascending=False)
bars = plt.bar(avg_volume_by_country.index, avg_volume_by_country.values, color='gold')
plt.title('Средний объем двигателя по странам производства', fontsize=16, fontweight='bold')
plt.xlabel('Страна производства', fontsize=12)
plt.ylabel('Средний объем двигателя (л)', fontsize=12)
plt.show()

plt.hist(df['Год_выпуска'], bins=range(1995, 2025, 2), edgecolor='black', color='lightblue', alpha=0.7)
plt.title('Распределение автомобилей по годам выпуска', fontsize=16, fontweight='bold')
plt.xlabel('Год выпуска', fontsize=12)
plt.ylabel('Количество автомобилей', fontsize=12)
plt.show()

top_10_brands = df['Марка'].value_counts().head(10).index
df_top10 = df[df['Марка'].isin(top_10_brands)]
avg_age_by_brand = df_top10.groupby('Марка')['Лет_с_выпуска'].mean().sort_values()

bars = plt.barh(avg_age_by_brand.index, avg_age_by_brand.values, color='lightpink')
plt.title('Средний возраст автомобилей по маркам (топ-10)', fontsize=16, fontweight='bold')
plt.xlabel('Средний возраст (лет)', fontsize=12)
plt.ylabel('Марка автомобиля', fontsize=12)
plt.show()

top_5_brands = df['Марка'].value_counts().head(5)
plt.pie(top_5_brands.values, labels=top_5_brands.index, autopct='%1.1f%%')
plt.title('Топ-5 самых распространенных марок автомобилей', fontsize=16, fontweight='bold')
plt.show()

df.to_csv('cars.csv', index=False, encoding='utf-8-sig')
print(f"\nДанные сохранены в файл 'cars.csv'")
print(f"Всего сохранено {len(df)} записей")

print("\n" + "="*80)
print("СТАТИСТИКА ПО СТРАНАМ ПРОИЗВОДСТВА:")
print("="*80)
for country in df['Страна'].unique():
    country_df = df[df['Страна'] == country]
    print(f"\n{country}:")
    print(f"  Количество автомобилей: {len(country_df)}")
    print(f"  Марки: {', '.join(country_df['Марка'].unique())}")
    print(f"  Средняя мощность: {country_df['Лошадиные_силы'].mean():.1f} л.с.")
    print(f"  Средний объем: {country_df['Объем_двигателя'].mean():.1f} л")
    print(f"  Средний возраст: {country_df['Лет_с_выпуска'].mean():.1f} лет")

newest_car = df.loc[df['Лет_с_выпуска'].idxmin()]
oldest_car = df.loc[df['Лет_с_выпуска'].idxmax()]

print("\n" + "="*80)
print(f"\nСамый новый автомобиль: {newest_car['Марка']} {newest_car['Год_выпуска']}г. ({newest_car['Лошадиные_силы']} л.с.)")
print(f"Самый старый автомобиль: {oldest_car['Марка']} {oldest_car['Год_выпуска']}г. ({oldest_car['Лошадиные_силы']} л.с., возраст: {oldest_car['Лет_с_выпуска']} лет)")
print(f"\nСамый мощный автомобиль: {df.loc[df['Лошадиные_силы'].idxmax()]['Марка']} ({df['Лошадиные_силы'].max()} л.с.)")
print(f"Самый большой объем двигателя: {df.loc[df['Объем_двигателя'].idxmax()]['Марка']} ({df['Объем_двигателя'].max():.1f} л)")