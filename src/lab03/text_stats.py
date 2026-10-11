from src.lib.text import normalize, tokenize, count_freq, top_n
text=input()

normal_text=normalize(text)
token_text=tokenize(normal_text)
freq_text=count_freq(token_text)
top_text=top_n(freq__text)
print(normal_text,token_text,freq_text,top_text)
