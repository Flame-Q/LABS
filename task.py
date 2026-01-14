import random
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

fake = Faker('ru_RU')

years = [2021, 2022, 2023, 2024, 2025]
forms = ['Бюджет', 'Платное']
specialties = ['Информатика', 'Экономика', 'Право', 'Медицина', 'Филология']

data = []
for _ in range(200):
    year = random.choice(years)
    form = random.choice(forms)
    specialty = random.choice(specialties)
    ct_score = random.randint(150, 300)
    avg_grade = round(random.uniform(6, 10), 1)
    total_score = int(ct_score + avg_grade * 10)
    data.append({
        'ФИО': fake.name(),
        'Год поступления': year,
        'Форма обучения': form,
        'Балл ЦТ/ЦЭ': ct_score,
        'Средний балл аттестата': avg_grade,
        'Общий балл': total_score,
        'Специальность': specialty,
        'Адрес': fake.address().replace('\n', ', '),
        'Телефон': fake.phone_number()
    })

df = pd.DataFrame(data)

print("Все сгенерированные данные студентов:")
print(df.to_string(index=False))

with open("students.txt", "w", encoding="utf-8") as f:
    f.write(df.to_string(index=False))
print("Данные сохранены в файл 'students.txt'")

avg_ct = df.groupby('Год поступления')['Балл ЦТ/ЦЭ'].mean()
x = avg_ct.index.to_numpy()
y = avg_ct.to_numpy()
plt.plot(x, y, label="Средний балл ЦТ/ЦЭ", color="blue")
plt.xlabel("Год поступления")
plt.ylabel("Средний балл ЦТ/ЦЭ")
plt.title("Динамика среднего балла ЦТ/ЦЭ по годам")
plt.legend()
plt.show()

avg_att = df.groupby('Год поступления')['Средний балл аттестата'].mean()
x = avg_att.index.to_numpy()
y = avg_att.to_numpy()
plt.plot(x, y, label="Средний балл аттестата", color="green")
plt.xlabel("Год поступления")
plt.ylabel("Средний балл аттестата")
plt.title("Динамика среднего балла аттестата")
plt.legend()
plt.show()

min_total = df.groupby('Год поступления')['Общий балл'].min()
x = min_total.index.to_numpy()
y = min_total.to_numpy()
plt.plot(x, y, label="Минимальный общий балл (проходной)", color="red")
plt.xlabel("Год поступления")
plt.ylabel("Минимальный общий балл")
plt.title("Динамика проходного балла (минимального)")
plt.legend()
plt.show()

spec_count = df['Специальность'].value_counts()
x = spec_count.index.tolist()
y = spec_count.values.tolist()
plt.bar(x, y, label="Количество студентов", color='blue')
plt.xlabel("Специальность")
plt.ylabel("Количество студентов")
plt.title("Количество поступивших студентов по специальностям")
plt.legend()
plt.show()

form_count = df['Форма обучения'].value_counts()
x = form_count.index.tolist()
y = form_count.values.tolist()
plt.bar(x, y, label="Количество по форме обучения", color=['green', 'blue'])
plt.xlabel("Форма обучения")
plt.ylabel("Количество студентов")
plt.title("Статистика по формам обучения")
plt.legend()
plt.show()
