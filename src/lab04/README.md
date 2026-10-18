# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике
## Задание A — модуль src/lab04/io_txt_csv.py
### read_text
Функция читает весь текст файла и возвращает одной строкой.

По умолчанию стоит кодировка utf-8. Чтобы изменить, нужно прописать при вызове (пример: read_text("text.txt", encoding="cp1251") )

Падает на ошибках FileNotFoundError (файла не существует) и UnicodeDecodeError (неверная кодировка)
```python
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Возвращает весь текст файла в одну строку.
    
    По умолчанию стоит кодировка utf-8. Чтобы изменить, нужно прописать при вызове (пример: read_text("text.txt", encoding="cp1251") )

    Ошибки
        FileNotFoundError: файла не существует
        UnicodeDecodeError: неверная кодировка
    """
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)
```
-------
### ensure_parent_dir
Cоздает родительские директории, если их нет
```python
def ensure_parent_dir(path: str | Path) -> None:
    p=Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
```
---

### write_csv
Функция принимает список из строк таблицы, путь, где создаст csv, и заголовок таблицы (если есть); проверяет прямоугольность таблицы; перезаписывает строки в csv (если есть заголовок, пишет его первой строкой)
``` python
from pathlib import Path
import csv  
    
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Перезаписывает csv с разделителем ",". 
    Если есть заголовок таблицы (header), записывает его первой строкой
    
    Ошибки:
        ValueError: строки разной длины
    """
    p = Path(path)
    rows = list(rows)

    if len(rows)>0:
        if header is not None and len(header)!=len(rows[0]):
            raise ValueError("header другой длины")
        for x in rows:
            if len(x)!=len(rows[0]):
                raise ValueError("строки разной длины")

    ensure_parent_dir(p)
    
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
---
### Тесты
``` python
from src.lab04.io_txt_csv import read_text, write_csv
if __name__ == "__main__":
    txt = read_text("data/lab04/input1.txt")  
    print(txt) # возвращает строку
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создает CSV
```
Если в файле `"Привет, мир! Привет!!!"`:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/1_read_text.jpg?raw=true)
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/1_write_csv.jpg?raw=true)

Если в файле пусто:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/1_empty.jpg?raw=true)

Если файл отсутствует:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/1_no_fail.jpg?raw=true)

---

## Задание B — скрипт src/lab04/text_report.py
### text_report
Функция читает текст (если файла нет, пишет `файл не найден` и прекращается,); с помощью функций `normalize, tokenize, count_freq, top_n` из лаб3 обрабатывает текст и выводит в консоль кол-во всех слов, уникальных слов и топ-5; создает таблицу в csv с колонками `word,count` со всеми словами текста (count ↓, слово ↑ (при равенстве))
```python
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
INPUT_TEXT="data/lab04/input.txt"

def text_report():
    try:
        text=read_text(INPUT_TEXT, encoding="utf-8")
    except FileNotFoundError:
        print("файл не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print("неверная кодировка")
        sys.exit(1)

    norm_text=normalize(text)
    token=tokenize(norm_text)
    freq=count_freq(token)
    top_5=top_n(freq,5)

    print(f"Всего слов: {len(token)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word,count in top_5:
        print(f"{word}:{count}")
    
    top=sorted(freq.items(),key=lambda p: (-p[1],p[0]))
    write_csv(top, "data/lab04/report.csv", header=("word","count"))

if __name__=="__main__":
    text_report()
```

### Тесты
Если в файле `"Привет, мир! Привет!!!"`:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/2_text_report.jpg?raw=true)
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/2_text_report_csv.jpg?raw=true)

Если в файле пусто:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/2_empty.jpg?raw=true)
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/2_empty_csv.jpg?raw=true)

Если файл отсутствует:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/2_no_fail.jpg?raw=true)

