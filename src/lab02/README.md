# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)
## Задание №1 — arrays.py
### min_max
Возвращает кортеж (минимум, максимум).  Ловит ошибку "Список пуст".
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """кортеж из минимального и максимального чисел
    [3,-1,5,5,0] → (-1,5)
    """
    if len(nums)==0:
        raise ValueError("Список пуст")
    minimum=10**12
    maximum=-10**12
    for x in nums:
        if x<minimum:
            minimum=x
        if x>maximum:
            maximum=x
    return (minimum, maximum)

if __name__=="__main__":
    print(min_max([3,-1,5,5,0]))
    print(min_max([42]))
    print(min_max([-5,-2,-9]))
    print(min_max([1.5,2,2.0,-3.1]))  
    print(min_max([]))  
```

![](https://github.com/uswqs/python_labs/blob/main/images/lab02/arrays_min_max.png?raw=true) 


### unique_sorted
Возвращает отсортированный список уникальных значений (по возрастанию). 

Берём уникальные элементы через set. Для каждого элемента ищем в уже отсортированном result первое место, где элемент больше него, и вставляем туда. Если такого нет — вставляем в конец.
``` python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """отсортированный список уникальных значений (по возрастанию)
    [3, 1, 2, 1, 3] → [1, 2, 3]
    """
    unique_nums=list(set(nums))
    result=[]
    for x in unique_nums:
        index=len(result)
        for ind in range(len(result)):
            if result[ind]>x:
                index=ind
                break
        result.insert(index,x)
    return result

if __name__=="__main__":
    print(unique_sorted([3, 1, 2, 1, 3]))
    print(unique_sorted([]))
    print(unique_sorted([-1, -1, 0, 2, 2]))
    print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab02/arrays_unique_sorted.png?raw=true)


### flatten
«Расплющивает» список списков/кортежей в один список по строкам (row-major). 

Ловит ошибку "Строка вместо ряда", если встретилась строка/элемент, который не является списком/кортежем.
``` python
def flatten(mat: list[list | tuple]) -> list:
    """«расплющивает» список списков/кортежей в один список по строкам
    [[1, 2], (3, 4, 5)] → [1, 2, 3, 4, 5]
    """
    result=[]
    for row in mat:
        if isinstance(row, str):
            raise TypeError("Строка вместо ряда")
        for x in row:
            result.append(x)
    return result

if __name__=="__main__":
    print(flatten([[1, 2], [3, 4]]))
    print(flatten([[1, 2], (3, 4, 5)]))
    print(flatten([[1], [], [2, 3]]))
    print(flatten([[1, 2], "ab"]))
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab02/arrays_flatten.png?raw=true)


## Задание №2 — matrix.py
### transpose
Меняет строки и столбцы местами. Ловит "Рваные матрицы".

Внешний цикл i — по столбцам (каждый станет новой строкой), внутренний j — по строкам.

``` python
def transpose(mat: list[list[float | int]]) -> list[list]:  
    """меняет строки и столбцы местами
    [[1, 2, 3]] → [[1], [2], [3]]
    """
    if len(mat)==0:
        return []
    num_rows=len(mat)
    num_columns=len(mat[0])
    for row in mat:
        if len(row)!=num_columns:
            raise ValueError ("Рваная матрица")
    result = []
    for i in range(num_columns):
        row = []
        for j in range(num_rows):
            row.append(mat[j][i])
        result.append(row)
    return result

if __name__=="__main__":
    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
    print(transpose([[1, 2], [3, 4]]))
    print(transpose([]))
    print(transpose([[1, 2], [3]]))
```

![](https://github.com/uswqs/python_labs/blob/main/images/lab02/matrix_transpose.png?raw=true)


### row_sums
Считает сумму по каждой строке. Ловит "Рваные матрицы".

``` python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждой строке
    [[1, 2, 3], [4, 5, 6]] → [6, 15]
    """
    num_columns=len(mat[0])
    result=[]
    for row in mat:
        if len(row)!=num_columns:
            raise ValueError("Рваная матрица")
        result.append(sum(row))
    return result

if __name__=="__main__":
    print(row_sums([[1, 2, 3], [4, 5, 6]]))
    print(row_sums([[-1, 1], [10, -10]]))
    print(row_sums([[0, 0], [0, 0]]))
    print(row_sums([[1, 2], [3]]))
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab02/matrix_row_sums.png?raw=true)

### col_sums
Считает сумму по каждому столбцу. Ловит "Рваные матрицы".

Создаём список нулей нужной длины, идём по строкам и прибавляем каждый элемент к сумме соответствующего столбца.

``` python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждому столбцу
    [[1, 2, 3], [4, 5, 6]] → [5, 7, 9]
    """
    num_columns=len(mat[0])
    result=[0]*num_columns
    for row in mat:
        if len(row)!=num_columns:
            raise ValueError("Рваная матрица")
        for j in range(len(row)):
            result[j]+=row[j]
    return result

if __name__=="__main__":
    print(col_sums([[1, 2, 3], [4, 5, 6]]))
    print(col_sums([[-1, 1], [10, -10]]))
    print(col_sums([[0, 0], [0, 0]]))
    print(col_sums([[1, 2], [3]]))
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab02/matrix_col_sums.png?raw=true)


## Задание №3 — tuples.py
### format_record
Перезаписывает данные студента по форме. Ловит ошибки: "Пустое имя/группа/GPA", "Неверный тип ФИО/группы/GPA", "ФИО должно содержать 2-3 слова" если не полностью введено ФИО.

Разделяем ФИО по пробелам (должно быть 2 или 3 слова), собираем сокращённое ФИО необходимого регистра.
``` python
def format_record(rec: tuple[str, str, float]) -> str:
    """перезаписывает данные студента по форме
    ("Иванов Иван Иванович", "BIVT-25", 4.6) → "Иванов И.И., гр. BIVT-25, GPA 4.60"
    """
    fio,group,gpa = rec
    if len(fio.strip())==0:
        raise ValueError("Пустое имя")
    if not isinstance(fio, str):
        raise TypeError("Неверный тип ФИО")
    if len(group)==0:
        raise ValueError("Пустая группа")
    if not isinstance(group, str):
        raise TypeError("Неверный тип группы")
    if not gpa:
        raise ValueError("Пустой GPA")
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
```
![](https://github.com/uswqs/python_labs/blob/main/images/lab02/tuples_format_record.png?raw=true)
