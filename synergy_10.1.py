pets = {}

name = input("имя питомца: ")
animal_type = input("Вид питомца: ")
age = int(input("Возраст питомца: "))
owner_name = input("Имя владельца: ")

if age % 10 == 1 and age % 100 != 11:
    year_word = "год"
elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 > 20):
    year_word = "года"
else:
    year_word = "лет"

pets[name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": age,
    "Имя владельца": owner_name,
}


for pet_name, pet_info in pets.items():
    print(
        f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_info['Возраст питомца']} {year_word}. Имя владельца: {pet_info['Имя владельца']}"
    )
