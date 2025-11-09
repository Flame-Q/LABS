import numpy as np

expenses = np.array([50, 32, 62, 47, 54, 38, 45, 65, 36, 58, 27, 30])

winter = expenses[0] + expenses[1] + expenses[11]
summer = expenses[5] + expenses[6] + expenses[7]
print(f"Расходы в зимний период: {winter}")
print(f"Расходы в летний период: {summer}")

if winter > summer:
    print("В зимний период расходы на проезд больше")
elif winter < summer:
    print("В летний период расходы на проезд больше")
else:
    print("Расходы в зимний и летний период одинаковы")

max_expenses = np.max(expenses)
max_months = np.argmax(expenses)
print(f"Наибольшие расходы: {max_expenses} в {max_months} месяце")