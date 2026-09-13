n=int(input("Число участников: "))
offline=0
online=0
for i in range(n):
    person=input("Участник: ").split()
    if person[3]=='True':
        offline+=1
    else:
        online+=1
print(f"{offline} {online}")