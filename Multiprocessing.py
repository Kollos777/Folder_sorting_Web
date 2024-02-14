import multiprocessing
import time


def factorize(*numbers):
    results = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        results.append(factors)
    return results


def main():
    start_time = time.time()
    factorize(128, 255, 99999, 10651060)
    sync_time = time.time() - start_time
    print("Sync Time:", sync_time)
    start_time = time.time()

    num_cpus = multiprocessing.cpu_count()
    with multiprocessing.Pool(num_cpus) as pool:
        start = time.time()
        pool.map(factorize, (128, 255, 99999, 10651060))
        end = time.time()
        async_time = end - start
        print("Async Time:", async_time)


if __name__ == '__main__':
    main()
