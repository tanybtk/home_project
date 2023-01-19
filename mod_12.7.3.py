per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Пожалуйста, введите сумму депозита "))

deposit = [per_cent['ТКБ'] * money / 100, per_cent['СКБ'] * money / 100, per_cent['ВТБ'] * money / 100, per_cent['СБЕР'] * money / 100]
max_value = max(deposit)

print("Максимальная сумма, которую вы можете заработать составляет " + str(deposit) + "руб. max = " + str(max_value))
