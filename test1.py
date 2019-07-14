import time
import concurrent.futures
typ = 'process' 


def big_function(x):
    n = 50000000 - x
    c = 0
    for i in range(n):
        c += x
    return c

def main():
    a = [1, 2, 3]
    start = time.time()
    if typ == 'seq':
        res  = []
        for i in a:
            res.append(big_function(i))
    elif typ == 'process':
        with concurrent.futures.ProcessPoolExecutor() as executor:
            res = executor.map(big_function, a)
    elif typ == 'thread':
        with concurrent.futures.ThreadPoolExecutor() as executor:
            res = executor.map(big_function, a)
    end = time.time()

    print(f'res: {list(res)} time: {end-start}')


if __name__ == "__main__":
    main()
