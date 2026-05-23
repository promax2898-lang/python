print()
print("Задание №1")
print()
num = int(input("Введите число: "))
for i in range(1, 11):
    print(num, "x", i, "=", (num * i))

print()
print("Задание №2")
print("Счёт в обратную сторону")
print()

print("Число от N до 1")
num = int(input("Введите число: "))
for i in range(num, 0, -1):
    print(i)
print("Кто не спрятался, я не виноват!!!")