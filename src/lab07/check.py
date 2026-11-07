import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def check_sorting(fn, trials=100):
    """сравнивает fn(nums) со sorted(nums)"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    return trials
    
def check_search(trials=100):
    """сравнивает linear_search и binary_search с list.index"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-150, 150)
        sorted_nums = sorted(nums)

        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        assert linear_search(nums, x) == expected, f"linear_search ошиблась на {nums}, x = {x}"
        
        result_binary = binary_search(sorted_nums, x)
        if result_binary != -1:
            assert  0 <= result_binary < len(sorted_nums), f"индекс вне диапазона {len(sorted_nums)}: функция выдала {result_binary}"
            assert sorted_nums[result_binary] == x, f"binary_search ошиблась на {nums}, x = {x}"
        else:
            assert x not in sorted_nums, f"binary_search не нашла {x} в {sorted_nums}"
    return trials

def check_two_sum(trials=100):
    """ оба способа должны давать пару с нужной суммой или оба None
    
    при расхождении — AssertionError с данными, на которых разошлось"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        x = random.randint(-200, 200)

        res_brute = two_sum_brute(nums, x)
        res_fast  = two_sum_fast(nums, x)
        expected = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == x:
                    expected.append((i, j))
        if expected:
            assert res_brute in expected, f"two_sum_brute ошибся на {nums}, target = {x}"    
            assert res_fast in expected, f"two_sum_fast ошибся на {nums}, target = {x}"    
        
        else:            
            assert res_brute is None, f"two_sum_brute нашел результат, хотя ожидалось None"
            assert res_fast is None, f"two_sum_fast нашел результат, хотя ожидалось None"
    return trials

if __name__ == "__main__":
    random.seed(42)
    total_check = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total_check += check_sorting(fn)
    total_check += check_search()
    total_check += check_two_sum()
    print(f"OK, всего проверок {total_check}")