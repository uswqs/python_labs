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

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))


import re
def tokenize(text: str) -> list[str]:
    """Разбить на «слова» по небуквенно-цифровым разделителям
    
    "hello,world!!!" → ["hello", "world"]

    "по-настоящему круто" → ["по-настоящему", "круто"]

    "2025 год" → ["2025", "год"]
    """
    result=normalize(text)
    return re.findall(r"\w+(?:-\w+)*",result)

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитать частоты, вернуть словарь слово → количество.
    
    ["a","b","a","c","b","a"] → {"a":3,"b":2,"c":1}
    """
    dict={}


# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова.
    
    
    """

# print(top_n(["a","b","a","c","b","a"]))
# print(top_n(["bb","aa","bb","aa","cc"]))