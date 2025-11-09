import numpy as np

length_str = input("Введите длины участков: ")
speed_str = input("Введите средние скорости на участках: ")
length = length_str.split()
speed = speed_str.split()

k = int(input("Введите номер участка, на котором автомобиль въехал на дорогу (k): "))
p = int(input("Введите номер участка, после которого автомобиль выехал (p): "))

lengths = np.array(length, dtype=float)
speeds = np.array(speed, dtype=float)

distance = np.sum(lengths[k:p+1])

time = np.sum(lengths[k:p+1] / speeds[k:p+1])

average_speed = distance / time

print("Результаты:")
print(f"S = {distance:.2f} км")
print(f"T = {time:.2f} час")
print(f"V = {average_speed:.2f} км/ч")