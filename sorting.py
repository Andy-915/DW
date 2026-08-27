"""
Problem 6: Comparison of Different Sorting Algorithms
Six sorting algorithms: Insertion, Shell, Bubble, Quick, Selection, Heap
"""
import time
import random


# ─── 1. Direct Insertion Sort ────────────────────────────────────────────────
def insert_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ─── 2. Shell Sort ───────────────────────────────────────────────────────────
def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a


# ─── 3. Bubble Sort ──────────────────────────────────────────────────────────
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


# ─── 4. Quick Sort ───────────────────────────────────────────────────────────
def quick_sort(arr):
    a = arr[:]
    _quick_sort(a, 0, len(a) - 1)
    return a


def _quick_sort(a, low, high):
    if low < high:
        pi = _partition(a, low, high)
        _quick_sort(a, low, pi - 1)
        _quick_sort(a, pi + 1, high)


def _partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


# ─── 5. Simple Selection Sort ────────────────────────────────────────────────
def select_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# ─── 6. Heap Sort ────────────────────────────────────────────────────────────
def heap_sort(arr):
    a = arr[:]
    n = len(a)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _heapify(a, i, 0)
    return a


def _heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        _heapify(a, n, largest)


# ─── Menu and Main ───────────────────────────────────────────────────────────
ALGORITHMS = {
    1: ("Direct Insertion Sort", insert_sort),
    2: ("Shell Sort",            shell_sort),
    3: ("Bubble Sort",           bubble_sort),
    4: ("Quick Sort",            quick_sort),
    5: ("Simple Selection Sort", select_sort),
    6: ("Heap Sort",             heap_sort),
}


def benchmark(arr, runs=5):
    """Run all 6 algorithms and return timing results."""
    results = {}
    for key, (name, func) in ALGORITHMS.items():
        times = []
        for _ in range(runs):
            start = time.perf_counter()
            sorted_arr = func(arr)
            elapsed = time.perf_counter() - start
            times.append(elapsed)
        avg = sum(times) / runs
        results[name] = (avg, sorted_arr)
    return results


def main():
    print("=== Sorting Algorithm Comparison ===\n")

    # Small demo
    demo = [64, 34, 25, 12, 22, 11, 90, 45, 3, 78]
    print(f"Original sequence: {demo}\n")

    print(f"{'Algorithm':<25} | {'Sorted Result'}")
    print("-" * 70)
    for key, (name, func) in ALGORITHMS.items():
        result = func(demo)
        print(f"{name:<25} | {result}")

    # Performance comparison with larger array
    print("\n--- Performance Benchmark (n=2000, 5 runs avg) ---")
    large = random.sample(range(10000), 2000)
    bench = benchmark(large)
    print(f"\n{'Algorithm':<25} | {'Avg Time (ms)':>14}")
    print("-" * 44)
    for name, (avg, _) in sorted(bench.items(), key=lambda x: x[1][0]):
        print(f"{name:<25} | {avg*1000:>14.4f}")

    # Interactive menu
    print("\n--- Interactive Sorting ---")
    print("Select a sorting algorithm:")
    for k, (name, _) in ALGORITHMS.items():
        print(f"  {k}. {name}")
    print("  7. Run all algorithms")
    print("  0. Exit")

    try:
        choice = int(input("\nYour choice: "))
        if choice == 0:
            print("Exiting.")
            return
        raw = input("Enter numbers separated by spaces: ")
        arr = list(map(int, raw.split()))
        print(f"Original: {arr}")
        if choice == 7:
            for k, (name, func) in ALGORITHMS.items():
                print(f"{name}: {func(arr)}")
        elif choice in ALGORITHMS:
            name, func = ALGORITHMS[choice]
            print(f"{name}: {func(arr)}")
        else:
            print("Invalid choice.")
    except (ValueError, EOFError):
        print("Skipping interactive mode.")


if __name__ == "__main__":
    main()
