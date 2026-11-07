import timeit
import random
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def bench_sorts():
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        data = [random.randint(-10**6, 10**6) for _ in range(n)]
        t = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("sort", n, "sorted", f"{t:.6f}"))

        for func in (bubble_sort, insertion_sort, selection_sort):
            name = func.__name__
            if n <= 10_000:
                time = timeit.timeit(lambda: func(data), number = 1)
                rows.append(("sorting", n, name, f"{t:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))
    return rows

def bench_search():
    random.seed(42)
    rows = []
    data = [random.randint(-10**6, 10**6) for _ in range(100_000)]
    targets = [random.choice(data) for _ in range(10000)]
        
    t_lin = timeit.timeit(lambda: [linear_search(data, x) for x in targets], number=1)
    rows.append(("search", 100_000, "linear_search", f"{t_lin:.6f}"))
        
    sorted_data = sorted(data)
    t_bin = timeit.timeit(lambda: [binary_search(sorted_data, x) for x in targets], number=1)
    rows.append(("search", 100_000, "binary_search", f"{t_bin:.6f}"))
    return rows

def bench_2sum():
    random.seed(42)
    rows = []
    
    for n in (1_000, 10_000):
        data = [random.randint(-10**6, 10**6) for _ in range(n)]
        a, b = random.sample(data, 2)
        target = a + b

        t_2sb = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_brute", f"{t_2sb:.6f}"))

        t_2sf = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_fast", f"{t_2sf:.6f}"))
    
    return rows

def main():
    rows = bench_sorts() + bench_search() + bench_2sum()
    write_csv(rows, "data/lab07/bench.csv", ("задание", "n", "функция", "секунды"))

    max_len = 0
    for func in (bubble_sort, insertion_sort, selection_sort, linear_search, binary_search, two_sum_brute, two_sum_fast):
        name = func.__name__
        max_len = max(max_len, len(name))
    
    print(f"{'задание':<12} | {'n':<8} | {'функция':<{max_len}} | {'секунды':<12}")
    print("-" * (41 + max_len))
    for task, n, func, sec in rows:
        print(f"{task:<12} | {n:<8} | {func:<{max_len}} | {sec:<12}")

if __name__=="__main__":
    main()