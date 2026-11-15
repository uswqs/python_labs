import json
from pathlib import Path
from src.lib.io_helpers import ensure_parent_dir
from src.lab08.models import (
    make_student, 
    format_student,
    student_to_dict,
    student_from_dict
)

def students_to_json(students, path):
    """Сохраняет список записей в JSON"""
    data = [student_to_dict(s) for s in students]

    json_file = Path(path)
    ensure_parent_dir(json_file)

    with open(json_file, "w", encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path) -> list[dict]:
    json_file = Path(path)

    if not json_file.exists():
        raise FileNotFoundError("файл отсутствует")
    if json_file.suffix.lower() != ".json":
        raise ValueError("неверный тип файла, должен быть .json")

    with open(json_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        
    if not data:
        raise ValueError("пустой json файл")
    if not isinstance(data,list):
        raise ValueError("неверный тип данных")

    students = []
    skipped = []
    for number, raw in enumerate(data, start = 1):
        if not isinstance(raw, dict):
            skipped.append((number, "не словарь"))
            continue  
        try:        
            students.append(student_from_dict(raw))
        except (ValueError, TypeError) as e:
            skipped.append((number, str(e)))

    if skipped:
        print(f"Пропущено записей: {len(skipped)} из {len(data)}")
        for number, reason in skipped:
            print(f"  №{number}: {reason}")
        
    return students

def main():
    student1 = make_student("Иванов Иван Иванович", "2008-12-27", "БИВТ-25-6-15", 4.1)
    student2 = make_student("Николаев Андрей Викторович", "2008-03-18", "БИВТ-25-6-1", 3.5)
    # student3_bad = 
    students = [student1, student2]

    students_to_json(students, "data/lab08/students_output.json")
    
    print("Результаты функции students_from_json (правильный файл)")
    for student in students_from_json("data/lab08/students_input.json"):
        print(format_student(student))
    
    print(f"\nРезультаты функции students_from_json (битый файл)")
    for student in students_from_json("data/lab08/students_bad.json"):
        print(f"Студенты с верными данными:\n{format_student(student)}")

if __name__=="__main__":
    main()
