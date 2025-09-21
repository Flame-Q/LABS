base_min = 60
base_sms = 30
base_mb = 1024
base_price = 24.99

dop_min = 0.89
dop_sms = 0.59
dop_mb = 0.79

used_min = int(input("Использовано минут: "))
used_sms = int(input("Использовано SMS: "))
used_mb = int(input("Использовано МБ: "))

dop_min_cost = 0
if used_min > base_min:
    dop_min_cost = (used_min - base_min) * dop_min

dop_sms_cost = 0
if used_sms > base_sms:
    dop_sms_cost = (used_sms - base_sms) * dop_sms

dop_mb_cost = 0
if used_mb > base_mb:
    dop_mb_cost = (used_mb - base_mb) * dop_mb

sum = base_price + dop_min_cost + dop_min_cost + dop_mb_cost

tax = sum * 0.02
total = sum + tax

print("Базовая стоимость:", base_price, "руб.")

if dop_min_cost > 0:
    print("Доп. минуты:", dop_min_cost, "руб.")

if dop_sms_cost > 0:
    print("Доп. SMS:", dop_sms_cost, "руб.")

if dop_mb_cost > 0:
    print("Доп. интернет:", dop_mb_cost, "руб.")

print("Налог 2%:", tax, "руб.")
print("Итого к оплате:", total, "руб.")