import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv", help="Преобразует JSON-файл в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной файл")
    p1.add_argument("--out", dest="output", required=True, help="Файл вывода")

    p2 = sub.add_parser("csv2json", help="Преобразует CSV-файл в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной файл")
    p2.add_argument("--out", dest="output", required=True, help="Файл вывода")

    p3 = sub.add_parser("csv2xlsx", help="Преобразует CSV-файл в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной файл")
    p3.add_argument("--out", dest="output", required=True, help="Файл вывода")

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)     

if __name__=="__main__":
    main()