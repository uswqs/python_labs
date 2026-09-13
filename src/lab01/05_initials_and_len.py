fio=input("ФИО: ").split()
initials="".join(i[0] for i in fio)
print(f'Инициалы: {initials}')
fio="".join(fio)
print(f"Длина (символов): {len(fio)}")

