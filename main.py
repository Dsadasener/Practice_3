# Завдання для Учасника команди:
# Додати функцію пошуку співробітника за фрагментом адреси та додати відповідний пункт виклику цієї функції у головне меню програми
employees = {
    "Іванов": "вул. Хрещатик, 1",
    "Кузін": "вул. Шевченка, 15",
    "Петренко": "пр. Свободи, 12",
    "Куравльов": "вул. Франка, 8",
    "Сидоренко": "вул. Лесі Українки, 22",
    "Кудін": "пр. Науки, 5",
    "Коваленко": "вул. Перемоги, 10",
    "Кульков": "вул. Миру, 3",
    "Мельник": "вул. Садова, 7",
    "Кубиків": "пр. Будівельників, 4"
}

def print_all(emp_dict):
    for k, v in emp_dict.items():
        print(f"Співробітник: {k} - Адреса: {v}")

def add_record(emp_dict):
    key = input("Введіть прізвище: ")
    val = input("Введіть адресу: ")
    emp_dict[key] = val
    print("Додано", key, ".")

def del_record(emp_dict):
    key = input("Введіть прізвище для видалення: ")
    try:
        del emp_dict[key]
        print("Видалено", key, ".")
    except KeyError:
        print(f"Помилка: Співробітника з прізвищем '{key}' не знайдено у словнику")

def print_sorted(emp_dict):
    print("Відсортований словник: ")
    for k in sorted(emp_dict):
        print(f"Співробітник; {k} - Адреса: {emp_dict[k]}")

def check_variant_surnames(emp_dict):
    targets = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]
    found = False
    print("Результат пошуку за варіантом: ")
    for target in targets:
        if target in emp_dict:
            print(f"{target} працює у фірмі. Адреса: {emp_dict[target]}")
            found = True

    if not found:
        print("Жодного із зазначених співробітників не знайдено")

def search_by_address_fragment(emp_dict):
    fragment = input("Введіть фрагмент адреси для пошуку: ")
    found = False
    print("Результат пошуку за фрагментом адреси: ")
    for k, v in emp_dict.items():
        #Переводимо в нижній регістр для незалежності від регістру під час пошуку
        if fragment.lower() in v.lower():
            print(f"Співробітник: {k} - Адреса: {v}")
            found = True

    if not found:
        print("Співробітників за вказаним фрагментом адреси не знайдено")

def main():
    while True:
        print("_" * 50)
        print("Головне меню")
        print(" 1 - Вивести всі значення словника")
        print(" 2 - Додати новий запис")
        print(" 3 - Видалити запис")
        print(" 4 - Переглянути словник за відсортованими ключами")
        print(" 5 - Пошук співробітників")
        print(" 6 - Пошук співробітника за фрагментом адреси") # Додано новий пункт
        print(" 0 - Вийти з програми")
        choice = input("Введіть пункт меню: ")

        print("_" * 50)

        if choice == '1':
            print_all(employees)
        elif choice == '2':
            add_record(employees)
        elif choice == '3':
            del_record(employees)
        elif choice == '4':
            print_sorted(employees)
        elif choice == '5':
            check_variant_surnames(employees)
        elif choice == '6':
            search_by_address_fragment(employees) # Додано виклик нової функції
        elif choice == '0':
            print("Роботу завершено")
            break
        else:
            # Оновлено текст помилки (від 0 до 6)
            print("Невірне значення, оберіть цифру від 0 до 6")

        print("-" * 50)
        input("Натисніть Enter, щоб повернутися до меню")

if __name__ == "__main__":
    main()
