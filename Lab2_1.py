summa = float(input("Введите сумму покупки: "))

if summa > 1000:
    discount = 5
    total = summa * (1 - discount / 100)
elif summa > 500:
    discount = 3
    total = summa * (1 - discount / 100)
else:
    discount = 0
    total = summa

print(f"Сумма покупки: {summa:.2f} руб.")
if discount > 0:
    print(f"Скидка: {discount}%")
    print(f"Сумма к оплате: {total:.2f} руб.")
else:
    print("Скидка не предоставляется")
    print(f"Сумма к оплате: {total:.2f} руб.")