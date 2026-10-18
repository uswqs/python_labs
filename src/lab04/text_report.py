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