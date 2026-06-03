print()
print("Задание №1")
print()

total = 0
while True:
    num1 = int(input("Введи число (0 для выхода): "))
    if num1 == 0:
        break
    total += num1
print("Сумма: ", total)

print()
print("Задание №2")
print()

num = int(input("Введите число: "))
while num > 0:
    print(num)
    num -= 1
print("Конец")
