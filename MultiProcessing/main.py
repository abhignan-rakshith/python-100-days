# import multiprocessing as mp
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds} second")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


if __name__ == '__main__':
    seconds = [6, 4, 3, 2, 1]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(do_something, seconds)

        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f"Finished in {finish - start:.2f} seconds")

# mp.freeze_support()
# processes = []
# for _ in range(10):
#     p = mp.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
#
# for p in processes:
#     p.join()
