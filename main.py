import os.path
import re

# Получаем путь к файлу names.txt
PATH_TO_TXT = os.path.join(os.getcwd(), "data", "names.txt")


def filter_name_from_txt(file_name):
    """Функция отсортировывает имена при этом удаляет числа и знаки припинания."""
    # Преобразуем текст в список
    # with open('data/'+file_name, "r", encoding="utf-8") as f: - альтернативный вариант
    with open(PATH_TO_TXT, "r", encoding="utf-8") as f:
        list_txt = f.readlines()

    new_name_list = []
    # new_name = ""
    # Проверяем слово на лишние символы и удаляем их.
    for name in list_txt:
        new_name = "".join(char for char in name if char.isalpha())
        new_name_list.append(new_name) if new_name != "" else None

    return new_name_list


def is_cirillic(name_item: str) -> bool:
    """Проверяем есть ли кириллица в слове"""
    return bool(re.search("[а-яА-Я]", name_item))


def filter_russian_names(names_list: list[str]) -> list[str]:
    """ "Фильтруем русские слова из списка"""
    new_list = []
    for name in names_list:
        if is_cirillic(name):
            new_list.append(name)
    return new_list


def filter_latin_names(names_list: list[str]) -> list[str]:
    """ "Фильтруем английские слова из списка"""
    new_list = []
    for name in names_list:
        if not is_cirillic(name):
            new_list.append(name)
    return new_list


def save_to_file(file_name: str, data: str) -> None:
    """ "Сохраняем список в файл"""
    with open("data/" + file_name, "w", encoding="utf-8") as names_file:
        names_file.write(data)


if __name__ == "__main__":
    filtered_list_names = filter_name_from_txt("names.txt")
    for i in filtered_list_names:
        print(i)

    save_to_file(
        "russian_words.txt", "\n".join(filter_russian_names(filtered_list_names))
    )
    save_to_file("latin_words.txt", "\n".join(filter_latin_names(filtered_list_names)))
