# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)
## Задание А — JSON ↔ CSV
- Модуль `src/lab05/json_csv.py`
- Функции `json_to_csv` и `csv_to_json`
____
### Функция `json_to_csv`
``` python 
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
        
    if not data:
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
7. Сохраняет в CSV (в кодировке UTF-8): первой записывает строку с заголовками, затем все строки файла

*Если в одном из словарей отсутствует ключ, csv.DictWriter записывает в соответствующую ячейку пустое значение.

**Запуск из терминала**
``` 
python -m src.lab05.json_csv
```
**Вызов функции**
```
json_to_csv("data\lab05\samples\people.json","data\lab05\out\people_from_json.csv")
```
**Вывод в `data.lab05.out.people_from_json.csv`**

![](https://github.com/uswqs/python_labs/blob/main/images/lab05/people_from_json.jpg?raw=true)
____

### Функция `csv_to_json`
```python
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

    if not data:
        raise ValueError("в CSV файле отсутствуют данные")

    ensure_parent_dir(json_file)

    with open(json_file, "w", encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent = 2)
```

**Что делает:**
1. Проверяет, есть ли файл
2. Проверяет, правильный ли формат файлов
3. Читает CSV файл 
4. Проверяет, есть ли заголовок
5. Создает список данных
6. Проверяет, есть ли данные в файле 
7. С помощью функции `ensure_parent_dir` (из лр4) проверяет наличие родительских директорий (или создает их в случае необходимости)
8. Сохраняет в JSON (в кодировке UTF-8) список словарей

*Благодаря `ensure_ascii=False` текст читаем для человека, а `indent=2` делает два отступа, чтобы было удобнее воспринимать информацию.

**Запуск из терминала**
``` 
python -m src.lab05.json_csv
```
**Вызов функции**
```
csv_to_json("data\lab05\samples\people.csv","data\lab\05\out\people_from_csv.json")
```

**Вывод в `data.lab05.out.people_from_csv.json`**

![](https://github.com/uswqs/python_labs/blob/main/images/lab05/people_from_csv.jpg?raw=true)
____

## Задание B — CSV → XLSX
- Модуль `src/lab05/csv_xlsx.py`
- Функция `csv_to_xlsx`
____
### Функция `csv_to_xlsx`
```python
from pathlib import Path
from openpyxl import Workbook
from src.lib.io_helpers import ensure_parent_dir
import csv

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file=Path(csv_path)
    xlsx_file=Path(xlsx_path)

    if not csv_file.exists():
        raise FileNotFoundError("файл отсутствует")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("неверный тип файла, должен быть .csv")
    if xlsx_file.suffix.lower() != ".xlsx":
        raise ValueError("неверный тип файла, должен быть .xlsx")

    with open(csv_file, "r", encoding = "utf-8", newline = "") as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("файл CSV пустой")
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in reader:
        ws.append(row)

    for column in ws.columns:
        max_len = 0
        letter = column[0].column_letter

        for cell in column:
            if cell.value is not None and len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))

        ws.column_dimensions[letter].width = max(max_len, 8)

    ensure_parent_dir(xlsx_file)
    wb.save(xlsx_file)
```
**Что делает:**
1. Проверяет, есть ли файл
2. Проверяет, правильный ли формат файлов
3. Читает CSV файл 
4. Создает книгу Excel с помощью openpyxl и лист Sheet1
5. Находит максимальную длину ячейки для каждого столбца и фиксирует ее (не менее 8 символов) 
6. С помощью функции `ensure_parent_dir` (из лр4) проверяет наличие родительских директорий (или создает их в случае необходимости)
8. Сохраняет результат по указанному пути


**Запуск из терминала**
``` 
python -m src.lab05.csv_xlsx
```
**Вызов функции**
```
csv_to_xlsx("data\lab05\samples\cities.csv","data\lab05\out\cities.xlsx")
```

**Вывод в `data.lab05.out.cities.xlsx`**

![](https://github.com/uswqs/python_labs/blob/main/images/lab05/cities.jpg?raw=true)