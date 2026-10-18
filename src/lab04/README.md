# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике
## Задание A — модуль src/lab04/io_txt_csv.py
### read_text
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
### write_csv
``` python
from pathlib import Path
import csv
from typing import Iterable, Sequence
from collections import Counter    
    
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Перезаписывает csv с разделителем ",". 
    Если есть строка заголовков таблицы (header), записывает ее первой строкой
    
    Ошибки:
        ValueError: строки разной длины
    """
    p = Path(path)
    rows = list(rows)

    if len(rows)>0:
        if header is not None:
            if len(header)!=len(rows[0]):
                raise ValueError("header другой длины")
        for x in rows:
            if len(x)!=len(rows[0]):
                raise ValueError("строки разной длины")

    p.parent.mkdir(parents=True, exist_ok=True)
    
    with p.open("w", newline="", encoding="utf-8") as f:
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
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/read_text.jpg?raw=true)
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/write_csv.jpg?raw=true)

Если в файле пусто:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/пустая_строка.jpg?raw=true)

Если файл отсутствует:
![](https://github.com/uswqs/python_labs/blob/main/images/lab04/нет_файла.jpg?raw=true)

---

## Задание B — скрипт src/lab04/text_report.py
### text_report
```python
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
input_text="data/lab04/input.txt"

def text_report():
    text=read_text(input_text, encoding="utf-8")

    norm_text=normalize(text)
    token=tokenize(norm_text)
    freq=count_freq(token)
    top_5=top_n(freq)

    print(f"Всего слов: {len(token)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word,count in top_5:
        print(f"{word}:{count}")
    
    top=sorted(freq.items(),key=lambda p: (-p[1],p[0]))
    write_csv(top, "data/lab04/report.csv", header=["word","count"])

if __name__=="__main__":
    text_report()
```

### Тесты
Если в файле `"Привет, мир! Привет!!!"`:
![]()

Если в файле пусто:
![]()

Если файл отсутствует:
![]()