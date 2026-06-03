import random




print("=" * 60)
print("||" + " " * 22 + "Число-мания" + " " * 22 + "||")
print("=" * 60)

print("\nМеню")

print("\nДоступные режимы игры:")
print("-" * 50)
print("1. Одиночная игра против компьютера")
print(" (Компьютер загадывает число от 1 до 100)")
print("2. Парная игра с другом")
print(" (Один игрок загадывает, второй угадывает)")
print("3. Выход из программы")
print("-" * 50)

while True:
    choice = input("\nВведите номер выбранного режима(1-3): ")
    if choice != "1" and choice != "2" and choice != "3":
        print("\nОшибка: нужно ввести 1, 2 или 3! Пожалуйста, попробуйте еще раз.")
        continue
    
    if choice == "1":
        print("Ты играешь с пк")
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
            
        print("Компьютер загадал число от 1 до 100. Попробуйте угадать!")
        while True:
            guess = int(input("Ваша догадка: "))
            attempts += 1
            if guess < secret_number:
                print("Загаданное число БОЛЬШЕ!")
            elif guess > secret_number:
                print("Загаданное число МЕНЬШЕ!")
            else:
                print(f"Поздравляем! Вы угадали за {attempts} попыток!")
                print(f"Вы заработали {max_attempts - attempts} очка/ов!")
                break
            if max_attempts and attempts >= max_attempts:
                print(f"Попытки закончились! Загаданное число было {secret_number}.")
                break
        
    elif choice == "2":
        print("Ты играешь с игроком")
        print("Игрок 1 загадывает число, Игрок 2 угадывает")
        secret_number = int(input("Игрок 1, введите число от 1 до 100: "))
        attempts = 0
        max_attempts = 10
                
        print("Игрок 2, начинайте угадывать!")
        while True:
            guess = int(input("Ваша догадка: "))
            attempts += 1
            if guess < secret_number:
                print("Загаданное число БОЛЬШЕ!")
            elif guess > secret_number:
                print("Загаданное число МЕНЬШЕ!")
            else:
                print(f"Игрок 2 угадал число за {attempts} попыток!")
                print(f"Игрок 2 заработал {max_attempts - attempts} очка/ов!")
                break
            if max_attempts and attempts >= max_attempts:
                print(f"Попытки закончились! Загаданное число было {secret_number}.")
                break
                
    elif choice == "3":
        print("Спасибо за игру! До свидания!")