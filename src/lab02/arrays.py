def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """кортеж из минимального и максимального чисел
    [3,-1,5,5,0] → (-1,5)
    """
    if len(nums)==0:
        raise ValueError("Список пуст")
    return (min(nums), max(nums))

if __name__=="__main__":
    print(min_max([3,-1,5,5,0]))
    print(min_max([42]))
    print(min_max([-5,-2,-9]))
    print(min_max([1.5,2,2.0,-3.1]))  
    print(min_max([]))   


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """отсортированный список уникальных значений (по возрастанию)
    [3, 1, 2, 1, 3] → [1, 2, 3]
    """
    return sorted(set(nums))

if __name__=="__main__":
    print(unique_sorted([3, 1, 2, 1, 3]))
    print(unique_sorted([]))
    print(unique_sorted([-1, -1, 0, 2, 2]))
    print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


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