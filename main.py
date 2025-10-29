import os.path
PATH_TO_TXT = os.path.join(os.getcwd(), "data", "names.txt")

def filter_name_from_txt(file_name):
    # with open('data/'+file_name, "r", encoding="utf-8") as f:
    with open(PATH_TO_TXT, "r", encoding="utf-8") as f:
        list_txt = f.readlines()
    print(list_txt)

    new_name_list = []
    signs = ".,!? \n@#№;:(){}[]"
    # new_name = ""
    for name in list_txt:
        new_name = "".join(char for char in name if char.isalpha())
        new_name_list.append(new_name) if new_name != "" else None

    return new_name_list


if __name__ == "__main__":
    filtered_list_names = filter_name_from_txt("names.txt")
    for i in filtered_list_names:
        print(i)
