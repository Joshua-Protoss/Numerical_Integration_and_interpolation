import multiprocessing as mp
#import numpy as np
import time
import worker

##def random_square(seed):
##    np.random.seed(seed)
##    random_num = np.random.randint(0, 10)
##    return random_num**2

t0 = time.time()

results = []

if __name__ ==  '__main__':
    n_cpu = mp.cpu_count()
    pool = mp.Pool(processes=n_cpu)
    results = pool.map(worker.random_square,range(10000000))

##for i in range(10000000):
##    results.append(worker.random_square(i))


t1 = time.time()

print(f'Execution time {t1-t0} s')
print(f"Number of cpu: {mp.cpu_count()}")
