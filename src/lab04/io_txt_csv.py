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
    try:
        p = Path(path)
    except FileNotFoundError:
        print("файл не найден")
        sys.exit(1)

    return p.read_text(encoding=encoding)


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

from src.lab04.io_txt_csv import read_text, write_csv
if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")  
    print(txt) # возвращает строку
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создает CSV