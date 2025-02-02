# Начальные значения
start1 = 2027
start2 = 1014

# Генерация последовательности
sequence = []

while start2 >= 1:
    sequence.append(start2)
    sequence.append(start1)
    start1 -= 1  # Уменьшаем первое значение
    start2 -= 1  # Уменьшаем второе значение

# Вывод последовательности
print(len(sequence))
print(sequence)
