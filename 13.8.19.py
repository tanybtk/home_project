tickets=int(input("При покупке от 4-х билетов, вы получаете скидку 10% от полной стоимости заказа.\nВведите количество билетов: "))

age = [0] * tickets

for idx in range(tickets):
    age[idx] = int(input("Введите возраст "+ str(idx + 1)+ ":"))
price = []
for i in age:
    if i in range(0, 18):
        price.append(0)
    elif i in range(18, 25):
        price.append(990)
    else:
        price.append(1390)
if tickets>3:
    sale = sum(price)-(sum(price)/100)*10
    print("Сумма со скидкой: ", sale, "руб.")
else:
    print("К оплате:", sum(price), "руб.")





