from src.lib.text import normalize, tokenize, count_freq, top_n
text=input()

normal_text=normalize(text)
token_text=tokenize(normal_text)
freq_text=count_freq(token_text)
top_text=top_n(freq_text)

print(f"Всего слов: {len(token_text)}")
print(f"Уникальных слов: {len(freq_text)}")
print(f"Топ-5:")
for x in range(len(top_text)):
    print(f"{top_text[x][0]}:{top_text[x][1]}")