from datetime import date
import re

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")
GROUP = re.compile(r"[А-ЯЁ]+(?:-\d+){3}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")

def validate_student(rec) -> None:
    """Валидация данных студента"""
    if not isinstance(rec, dict):
        raise TypeError("На входе должен быть словарь")
    if set(rec.keys()) != set(STUDENT_FIELDS):
        raise ValueError("Неверно введены данные")
    fio, birthdate, group, gpa = (rec[key] for key in STUDENT_FIELDS)
    
    if not isinstance(fio, str):
        raise TypeError("Неверный тип ФИО")
    fio = fio.strip()
    if len(fio) == 0:
        raise ValueError("Пустое имя")
    if len(fio.split()) > 3:
        raise ValueError("Лишние данные в ФИО")
    if len(fio.split()) < 2:
        raise ValueError("Недостаточно данных в ФИО, должны быть фамилия, имя (+ отчество при наличии)")
    
    if not isinstance(birthdate, str):
        raise TypeError("Неверный тип даты рождения, должна быть строка")
    birthdate = birthdate.strip()
    if len(birthdate) == 0:
        raise ValueError("Пустая дата рождения")
    if not DATE.fullmatch(birthdate):
        raise ValueError("Неверный формат даты рождения, должно быть YYYY-MM-DD")
    try:
        b = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError("Такой даты не существует")
    if b > date.today():
        raise ValueError('Дата рождения из будущего')
   
    if not isinstance(group, str):
        raise TypeError("Неверный тип группы")  
    group = group.strip()  
    if len(group)==0:
        raise ValueError("Пустая группа")
    if not GROUP.fullmatch(group):
        raise ValueError("Неверная запись группы, должен быть например БИВТ-26-6-4")

    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise TypeError(f"Неверный тип GPA")
    gpa = float(gpa)
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("Неправильное значение: должно быть 0.0<=GPA<=5.0")


def make_student(fio, birthdate, group, gpa) -> dict:
    """Создание словаря с данными студента"""
    rec = {
        "fio": fio,
        "birthdate": birthdate,
        "group": group,
        "gpa": gpa}
    validate_student(rec)

    rec["fio"] = fio.strip()
    rec["birthdate"] = birthdate.strip()
    rec["group"] = group.strip()
    rec["gpa"] = float(gpa)
    return (rec)

def student_age(rec, today=None) -> int:
    """Полных лет на дату today"""
    b = date.fromisoformat(rec["birthdate"])
    today = today or date.today()
    if (today.month, today.day) >= (b.month, b.day):
        return today.year - b.year
    else:
        return today.year - b.year - 1

def student_to_dict(rec):
    """Копия записи для сериализации, данные валидированы"""
    validate_student(rec)
    return {
        "fio": rec["fio"],
        "birthdate": rec["birthdate"],
        "group": rec["group"],
        "gpa": rec["gpa"]
    }

def student_from_dict(d):
    """Десериализация из словаря с валидацией"""    
    fio, birthdate, group, gpa = (d[key] for key in STUDENT_FIELDS)
    return make_student(fio, birthdate, group, gpa)


def format_student(rec):
    """Красивый вывод: Иванов И.И. БИВТ-26-6-1, 19 лет, GPA 4.30"""
    validate_student(rec)
    age = student_age(rec)

    fio = rec["fio"].split()
    surname = fio[0].capitalize()
    initials = ".".join(word[0].upper() for word in fio[1:]) + "."
    fio_new = f"{surname} {initials}"

    return f"{fio_new}, {rec['group']}, {age} лет, GPA {rec['gpa']:.2f}"