tasks = []
completed_tasks = []
while True:
    print("\n=== Легендарный помощник: список дел ===")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Показать выполненные задачи")
    print("6. Выйти")
 
    choice = input("Выберите пункт меню: ")
    
    if choice == "1":
        new_task = input("Введите новую задачу: ").strip()
        if new_task:
            tasks.append(new_task)
            print("Задача добавлена!")
        else:
            print("Нельзя добавить пустую задачу.")
            
    elif choice == "2":
        if tasks:
            print("Ваши задачи:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
        else:
            print("Список задач пуст.")
            
    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
                
            try:
                task_num = int(input("Введите номер выполненной задачи: "))
                if 1 <= task_num <= len(tasks):
                    completed = tasks.pop(task_num - 1)
                    completed_tasks.append(completed)
                    print(f"Задача '{completed}' выполнена")
                else:
                    print("Неверный номер задачи.")
            except ValueError:
                print("Введите число!")
        else:
            print("Список задач пуст.")
            
    elif choice == "4":
        if tasks:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
                
            try:
                task_num = int(input("Введите номер задачи для удаления: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Задача '{removed}' удалена.")
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Введите число!")
        else:
            print("Список задач пуст.")
            
    elif choice == "5":
        if completed_tasks:
            print("Выполненные задачи: ")
            for i, task in enumerate(completed_tasks):
                print(f"{i + 1}. {task}")
                
        
    elif choice == "6":
        print("До свидания!")
        break
    
    else:
        print("Такой команды нет! Введите номер от 1 до 6!")