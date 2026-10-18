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
    
    