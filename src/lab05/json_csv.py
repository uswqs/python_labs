from pathlib import Path
import csv 
import json
from src.lib.io_helpers import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError("файл отсутствует")
    if json_file.suffix.lower() != ".json":
        raise ValueError("неверный тип файла, должен быть .json")
    if csv_file.suffix.lower() != ".csv":
            raise ValueError("неверный тип файла, должен быть .csv")

    with open(json_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Пустой JSON или неподдерживаемая структура")
            sys.exit(1)
        
    if len(data) == 0:
        raise ValueError("пустой json файл")
    if not isinstance(data,list):
        raise ValueError("неверный тип данных")
    if not all(isinstance(item,dict) for item in data):
        raise ValueError("все данные должны быть словарями")

    ensure_parent_dir(csv_file)

    fieldnames = {}
    for x in data:
        for key in x.keys():
            fieldnames[key] = None
    
    with open(csv_file, "w", newline = "",encoding = "utf-8") as f:
        w = csv.DictWriter(f, fieldnames = fieldnames)
        w.writeheader()
        w.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not csv_file.exists():
        raise FileNotFoundError("файл отсутствует")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("неверный тип файла, должен быть .csv")
    if json_file.suffix.lower() != ".json":
        raise ValueError("неверный тип файла, должен быть .json")

    with open(csv_file, "r", encoding = "utf-8", newline = "") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("файл не содержит заголовок")

        data=list(reader)

    if len(data) == 0:
        raise ValueError("в CSV файле отсутствуют данные")

    ensure_parent_dir(json_file)

    with open(json_file, "w", encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent = 2)


if __name__=="__main__":
    json_to_csv("data\samples\people.json","data\out\people_from_json.csv")
    csv_to_json("data\samples\people.csv","data\out\people_from_csv.json")