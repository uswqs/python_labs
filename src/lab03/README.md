# ЛР3 — Тексты и частоты слов (словарь/множество)
## Задание A — src/lib/text.py
### normalize
``` python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """нормализированная строка (нижний регистр, ё->е, без лишних символов)

    "ёжик, Ёлка" (yo2e=True) → "ежик, елка"

    "ПрИвЕт\nМИр\t" → "привет мир""""
    s=""
    if casefold==True:
        s=text.casefold()
    else:
        s=text.lower()

    if yo2e==True:
        s=s.replace("ё","е")

    norm_s=" ".join(s.split())
    return norm_s
```
Тест-кейсы
```python
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab03/normalize.png?raw=true) 


### tokenize
``` python
import re
def tokenize(text: str) -> list[str]:
    """список из строк («слова» по небуквенно-цифровым разделителям)
    
    "hello,world!!!" → ["hello", "world"]

    "по-настоящему круто" → ["по-настоящему", "круто"]

    "2025 год" → ["2025", "год"]"""
    result=normalize(text)
    return re.findall(r"\w+(?:-\w+)*",result)
```
Тест-кейсы
```python
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab03/tokenize.png?raw=true) 

### count_freq
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    """словарь слово → количество
    
    ["a","b","a","c","b","a"] → {"a":3,"b":2,"c":1}"""
    freq={}
    for w in tokens:
        freq[w]=freq.get(w,0)+1
    return freq
```

Тест-кейсы
```python
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
```

### top_n
``` python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """список по убыванию частоты; при равенстве - по алфавиту слова.
    
    {'a': 3, 'b': 2, 'c': 1} -> [('a', 3), ('b', 2), ('c', 1)]"""
   
    top=sorted(freq.items(),key=lambda p: (-p[1],p[0]))[:n]
    return top
```
Тест-кейсы
```python
print(top_n({'a': 3, 'b': 2, 'c': 1}))
print(top_n({'bb': 2, 'aa': 2, 'cc': 1}))
```


## Задание B — src/text_stats.py

```python
from src.lib.text import normalize, tokenize, count_freq, top_n
text=input()

normal_text=normalize(text)
token_text=tokenize(normal_text)
freq_text=count_freq(token_text)
top_text=top_n(freq__text)

print(f"Всего слов: {len(token_text)}")
print(f"Уникальных слов: {len(freq_text)}")
print(f"Топ-5:")
for x in range(len(top_text)):
    print(f"{top_text[x][0]}:{top_text[x][1]}")```
    
