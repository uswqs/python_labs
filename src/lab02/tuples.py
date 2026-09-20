def format_record(rec: tuple[str, str, float]) -> str:
    fio,group,gpa = rec
    if len(fio.strip())==0:
        raise ValueError("Пустое имя")
    if not isinstance(fio, str):
            raise TypeError("Неверный тип ФИО")
    if len(group)==0:
        raise ValueError("Пустая группа")
    if not isinstance(group, str):
                raise TypeError("Неверный тип группы")
    if not isinstance(gpa, float):
        raise TypeError("Неверный тип GPA")

    fio_new=""

    fio=fio.split()
    if len(fio)<2 or len(fio)>3:
        raise ValueError("ФИО должно содержать 2-3 слова")
    if len(fio)==2:
        fio_new=fio[0][:1].upper() + fio[0][1:] + " " + fio[1][0].upper() + "."
    if len(fio)==3:
        fio_new=fio[0][:1].upper() + fio[0][1:] + " " + fio[1][0].upper() + "." + fio[2][0].upper() + "."

    return f"{fio_new}, гр. {group.strip()}, GPA {gpa:.2f}"

if __name__=="__main__":
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
    
    
    
    
    