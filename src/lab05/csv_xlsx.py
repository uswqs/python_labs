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

if __name__=="__main__":
    csv_to_xlsx("data\lab05\samples\cities.csv","data\lab05\out\cities.xlsx")