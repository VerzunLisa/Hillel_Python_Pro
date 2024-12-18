import multiprocessing


def partial_sum(numbers):
    """Функція для обчислення суми частини масиву."""
    return sum(numbers)


def parallel_sum(array, num_processes):
    """Функція для обчислення суми елементів великого масиву паралельно."""
    chunk_size = len(array) // num_processes
    chunks = [array[i * chunk_size:(i + 1) * chunk_size] for i in range(num_processes)]

    if len(array) % num_processes != 0:
        chunks[-1].extend(array[num_processes * chunk_size:])

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(partial_sum, chunks)

    return sum(results)


if __name__ == "__main__":
    large_array = [i for i in range(1, 10001)]
    num_processes = 4
    total = parallel_sum(large_array, num_processes)
    print(f"Сума елементів масиву: {total}")
