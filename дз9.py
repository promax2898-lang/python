name = input("Введите имя: ")
print("Привет", name, "!")

print()
print()
print()

try:
    num1 = int(input("Введите 1-ое число: "))
    num2 = int(input("Введите 2-ое число: "))
    print(f"{int(num1) / num2}")
    
except ZeroDivisionError:
    print("Ошибка: " + "на ноль делить нельзя.")
    
except ValueError:
    print("Ошибка: " + "вы ввели не число")