# ЛР3 — Тексты и частоты слов (словарь/множество)
## Задание A — src/lib/text.py
### normalize
``` python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """нормализированная строка (нижний регистр, ё->е, без лишних символов)

    "ёжик, Ёлка" (yo2e=True) → "ежик, елка"

    "ПрИвЕт\nМИр\t" → "привет мир"
    """
    if casefold==True:
        s=text.casefold()
    else:
        s=text.lower()

    if yo2e==True:
        s=s.replace("ё","е")

    s=s.strip()
    norm_s=" ".join(s.split())
    return norm_s
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab03/normalize.png?raw=true) 

### tokenize