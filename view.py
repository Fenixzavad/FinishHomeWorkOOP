import zoo

def menu():
    print("\n1. Добавить животное в Зоопарк\n"
          "2. Удалить животное из Зоопарка\n"
          "3. Просмотреть информацию о конкретном животном\n"
          "4. Слушить звук животного\n"
          "5. Просмотреть информацию о всех животных в Зоопарке\n"
          "6. Все животные в Зоопарке издают звуки\n"
          "7. Выйти")
    num = int(input("Выберите пункт меню: "))
    return num


def addAnimalMenu():
    print("\n1. Добавить кота\n"
          "2. Добавить тигра\n"
          "3. Добавить собаку\n"
          "4. Добавить волка\n"
          "5. Добавить курицу\n"
          "6. Добавить аиста\n"
          "7. Выйти")
    num = int(input("Выберите пункт меню: "))
    return num


def deleteAnimalMenu():
    print(f"{len(zoo.Zoo.all)+1} Назад")
    num = int(input("Выберите животное кого хотите удалить: "))
    return num


def showAnimalMenu():
    print(f"{len(zoo.Zoo.all)+1} Назад")
    num = int(input("Выберите животное которое хотите посмотреть: "))
    return num


def sayAnimalMenu():
    print(f"{len(zoo.Zoo.all)+1} Назад")
    num = int(input("Выберите  животное которое хотите услышать "))
    return num