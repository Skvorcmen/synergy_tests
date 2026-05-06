pets = {}


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 > 20):
        return "года"
    else:
        return "лет"


def get_pet(id):
    return pets[id] if id in pets else False


def pets_list():
    if not pets:
        print("База данных пуста.")
        return

    print()
    for pet_id, pet_info in pets.items():
        for pet_name, details in pet_info.items():
            suffix = get_suffix(details["Возраст питомца"])
            print(
                f"ID: {pet_id} - Это {details['Вид питомца']} по кличке \"{pet_name}\". "
                f"Возраст питомца: {details['Возраст питомца']} {suffix}. "
                f"Имя владельца: {details['Имя владельца']}"
            )


def get_last_id():
    if not pets:
        return 0
    return max(pets.keys())


def create():
    new_id = get_last_id() + 1

    print(f"(ID: {new_id})")
    name = input("Введите кличку питомца: ")
    animal_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": animal_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name,
        }
    }

    print(f"Питомец '{name}' успешно добавлен под ID {new_id}!")


def read():
    if not pets:
        print("База данных пуста. Сначала добавьте питомца командой 'create'.")
        return

    try:
        pet_id = int(input("Введите ID питомца для просмотра: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    pet_info = get_pet(pet_id)

    if pet_info is False:
        print(f"Питомец с ID {pet_id} не найден!")
        return

    for pet_name, details in pet_info.items():
        suffix = get_suffix(details["Возраст питомца"])
        print(
            f"Это {details['Вид питомца']} по кличке \"{pet_name}\". "
            f"Возраст питомца: {details['Возраст питомца']} {suffix}. "
            f"Имя владельца: {details['Имя владельца']}"
        )


def update():
    if not pets:
        print("База данных пуста. Сначала добавьте питомца командой 'create'.")
        return

    try:
        pet_id = int(input("Введите ID питомца для обновления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    pet_info = get_pet(pet_id)

    if pet_info is False:
        print(f"Питомец с ID {pet_id} не найден!")
        return

    print(f"Обновление информации о питомце (ID: {pet_id})")

    for pet_name, details in pet_info.items():
        print(
            f"Текущая информация: кличка: {pet_name}, вид: {details['Вид питомца']}, "
            f"возраст: {details['Возраст питомца']}, владелец: {details['Имя владельца']}"
        )

        new_name = input(f"Введите новую кличку (было: {pet_name}, Enter - оставить): ")
        new_animal_type = input(
            f"Введите новый вид питомца (было: {details['Вид питомца']}, Enter - оставить): "
        )
        new_age = input(
            f"Введите новый возраст (было: {details['Возраст питомца']}, Enter - оставить): "
        )
        new_owner = input(
            f"Введите новое имя владельца (было: {details['Имя владельца']}, Enter - оставить): "
        )

        updated_name = new_name if new_name else pet_name
        updated_details = {
            "Вид питомца": (
                new_animal_type if new_animal_type else details["Вид питомца"]
            ),
            "Возраст питомца": int(new_age) if new_age else details["Возраст питомца"],
            "Имя владельца": new_owner if new_owner else details["Имя владельца"],
        }

        pets[pet_id] = {updated_name: updated_details}

        print(f"Информация о питомце с ID {pet_id} успешно обновлена!")
        break


def delete():
    if not pets:
        print("База данных пуста. Нечего удалять.")
        return

    try:
        pet_id = int(input("Введите ID питомца для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    if pet_id in pets:
        for pet_name in pets[pet_id]:
            confirm = input(
                f"Вы уверены, что хотите удалить питомца '{pet_name}' с ID {pet_id}? (да/нет): "
            )
            if confirm.lower() == "да":
                del pets[pet_id]
                print(f"Питомец с ID {pet_id} успешно удалён!")
            else:
                print("Операция удаления отменена.")
            return

    print(f"Питомец с ID {pet_id} не найден!")


while True:
    command = input("\nВведите команду: ").strip().lower()

    if command == "stop":
        print("Работа программы завершена. До свидания!")
        break
    elif command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    else:
        print(
            "Неизвестная команда. Доступные команды: create, read, update, delete, list, stop"
        )
