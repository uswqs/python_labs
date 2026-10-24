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


def ensure_parent_dir(path: str | Path) -> None:
    p=Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


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
