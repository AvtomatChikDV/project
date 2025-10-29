import os.path

PATH_TO_TXT = os.path.join(os.getcwd(), "data", "names.txt")
with open(PATH_TO_TXT, "r", encoding="utf-8") as f:
    list_txt = f.readlines()
print(list_txt)

def filter_name_from_txt(name_list: list[str]) -> list[str]:
    new_name_list = []
    signs = ".,!? \n@#№;:(){}[]"
    # new_name = ""
    for name in name_list:
        new_name = "".join(
            char for char in name if char not in signs and not char.isdigit()
        )
        new_name_list.append(new_name) if new_name != "" else None

    return new_name_list


print(filter_name_from_txt(list_txt))
