list = ["молоко", "сыр", "яйца", "масло", "хлеб"]
for i in range(len(list)):
    print("Покупка " f"{i + 1}: {list[i]}")
    


while True:
    
    print()
    
    print("1. Удалить и добавить продукт")
    print("2. Выйти")
    
    print()
    
    choice = input("Выберите пункт меню: ")


    if choice == "1":
            print()
            num = input("Введите продукт для удаления: ")
            print()
            if num:
                removed = list.remove(num)
            new_list = input("Введите продукт для добавления: ")
            if new_list:
                list.append(new_list)
                print()
                print("Удалили: " + str(num))
                print("Добавили: " + str(new_list))
                print("Итоговый список: " + str(list))
            
    elif choice == "2":
            print()
            print("До свидания!")
            break

