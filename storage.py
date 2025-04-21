import os

DIR = "./storage/"

if not os.path.exists(DIR):
    os.makedirs(DIR)


def load_data(date):
    file_name = f"{DIR}{date[3:]}.txt"
    data = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                values = line.strip().split(";")
                data.append({
                    "date": values[0],
                    "type": values[1],
                    "amount": float(values[2]),
                    "comment": values[3]
                })

        return data
    except IOError as e:
        print(e)


def save_data(info):
    file_name = f"{DIR}{info["date"][3:]}.txt"
    result_line = ""
    try:
        with open(file_name, "a", encoding="utf-8") as f:
            for value in info.values():
                result_line += f"{value};"

            f.write(f"{result_line[:-1]}\n")
    except IOError as e:
        print(e)
