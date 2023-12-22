import numpy as np
# Параметри для моделі CRR
S0 = 12  # Поточна ціна акції
u = 1.3  # Фактор підйому
d = 0.9  # Фактор спуску
K = 15   # Ціна страйку
T = 3    # Кількість періодів

# Ризикова безрискова ставка не вказана, ми припускаємо її рівною r
r = 0.05  # Ризикова безрискова ставка

# Обчислимо ймовірність ризикового нейтралю
q = (np.exp(r) - d) / (u - d)

# Тепер обчислимо ціну європейської кол-опції за моделлю CRR

# Ініціалізація біноміального дерева цін
binomial_tree = np.zeros((T+1, T+1))

print(f"Binomial Tree: \n{binomial_tree}\n")

# Заповнимо біноміальне дерево цінами акцій
for i in range(T+1):
    for j in range(i+1):
        binomial_tree[j, i] = S0 * (u ** (i - j)) * (d ** j)
print(f"Binomail Tree after add actions price:\n {binomial_tree}\n")

# Обчислити значення опції на кожному кінцевому вузлі
option_value = np.maximum(binomial_tree[:, T] - K, 0)

# Відсортуємо значення опцій у зворотньому напрямку до поточного значення
for i in range(T-1, -1, -1):
    for j in range(i+1):
        option_value[j] = (q * option_value[j] + (1 - q) * option_value[j+1]) / np.exp(r)

print(f"Option value: {option_value}\n")

call_price = option_value[0]

# Використовуючи паритет кол-опцій для знаходження ціни опції на продажу (put option)
# put_price = call_price  - S0 + Поточне значення ціни страйку (K знижене на безрискову ставку r за час T)
put_price = call_price - S0 + (K / np.exp(r * T))

print(f"Q value: {q}\n")
print(f"Call Price: {call_price}\n")
print(f"Put Price: {put_price}\n")
