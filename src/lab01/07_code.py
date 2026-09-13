inn=(input("in: "))
word=[]
first=0
for i in range(len(inn)):
    if inn[i].isupper():
        word.append(inn[i])
        first=i
        break
second=0
for i in range(first,len(inn)):
    if inn[i].isdigit():
        second=i+1
        break
step=second-first
last_ind=0
for i in range(second,len(inn)):
    if inn[i]==".":
        last_ind=i
        break
for i in range(second,len(inn),step):
    if i<last_ind:
        word.append(inn[i])
rez="".join(word)+"."
print(rez)