# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)
## Задание А — JSON ↔ CSV
- Модуль `src/lab05/json_csv.py`
- Функции `json_to_csv` и `csv_to_json`
____
### Функция `json_to_csv`
``` python 
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
```
**Что делает:**
1. Проверяет, есть ли файл
2. Проверяет, правильный ли формат файлов
3. Читает JSON файл 
4. Проверяет, что файл не пустой и все данные - словари
5. С помощью функции `ensure_parent_dir` (из лр4) проверяет наличие родительских директорий (или создает их в случае необходимости)
6. Создает словарь с заголовками, записывая названия всех ключей в порядке их появления
7. Создает CSV (в кодировке UTF-8), первой записывает строку с заголовками, затем все строки файла

*Если в одном из словарей отсутствует ключ, csv.DictWriter записывает в соответствующую ячейку пустое значение.

**Запуск из терминала**
``` 
python -m src.lab05.json_csv
```
**Запуск функции**
```
json_to_csv("data\samples\people.json","data\out\people_from_json.csv")
```

