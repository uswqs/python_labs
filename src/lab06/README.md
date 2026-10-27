# ЛР6 — CLI‑утилиты с argparse (cat/grep‑lite + конвертеры)
## Задание 1
- Модуль `src/lab06/сli_text.py`
- Подкоманды `cat` (вывод содержимого файла построчно ) и `stats` (анализ частот слов в тексте)
```python
import argparse
from src.lib.io_helpers import read_text
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        rows = read_text(args.input).splitlines()
        if args.n:
            for num in range(1, len(rows)):
                print(f"{num} {rows[num-1]}")
        else:
            for row in rows:
                print(row)

    elif args.command == "stats":
        text=read_text(args.input)
        
        normal_text=normalize(text)
        token_text=tokenize(normal_text)
        freq_text=count_freq(token_text)
        top_text=top_n(freq_text, n = args.top)

        max_len_of_word=max((len(x[0]) for x in top_text))
        len_for_table=max(max_len_of_word, len("Слово"))

        print(f"Всего слов: {len(token_text)}")
        print(f"Уникальных слов: {len(freq_text)}")
        print(f"Топ-{args.top}:")
        print(f"{'Слово':<{len_for_table}} | частота:")
        print("-" * (len("Слово:")+ len_for_table + len(" | частота:")))
        for x in top_text:
            print(f"{x[0]:<{len_for_table}} : {x[1]}")

if __name__=="__main__":
    main()
```
___
**подкоманда cat**

Аргументы: 
- *"--input"* - входной файл
- *"-n"* - требуется ли нумерация строк

Вызов в терминале:
```
python -m src.lab06.cli_text cat --input data/lab06/samples/people.txt -n
```
Вывод:
![](https://github.com/uswqs/python_labs/blob/main/images/lab06/cli_text_cat.jpg?raw=true)
___

**подкоманда stats**

Аргументы: 
- *"--input"* - входной файл
- *"--top"* - количество значений при выводе таблицы с частотами (по умолчанию - 5)

Вызов в терминале:
```
python -m src.lab06.cli_text stats --input data/lab06/samples/people.txt --top 5
```
Вывод:
![](https://github.com/uswqs/python_labs/blob/main/images/lab06/cli_text_stats.jpg?raw=true)
___

## Задание 2
- Модуль `src/lab06/сli_convert.py`
- Подкоманды `json2csv`, `csv2json` и `csv2xlsx`
- Аргументы *"--in"* - входной файл, *"--out"*  - файл вывода
```python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)     

if __name__=="__main__":
    main()
```
