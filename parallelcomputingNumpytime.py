import numpy as np
import time
import multiprocessing as mp
  
def single_process_sum(arr):
    return np.sum(arr)

def worker(arr):
    return np.sum(arr)
  
def multi_process_sum(arr):
    num_processes = 10
    chunk_size = int(arr.shape[0] / num_processes)
    chunks = [arr[i:i + chunk_size] for i in range(0, arr.shape[0], chunk_size)]
    pool = mp.Pool(processes=num_processes)
    results = pool.map(worker, chunks)
  
    return sum(results)
  
if __name__ == '__main__':
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    start_time = time.perf_counter()
    result = multi_process_sum(arr)
    end_time = time.perf_counter()
      
    # calculating executing time
    total_time = end_time - start_time
    print(result)
    print(total_time)
    
  
##if __name__ == '__main__':
##    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
##      
##    start_time = time.perf_counter()
##    result = single_process_sum(arr)
##    end_time = time.perf_counter()
##      
##    # calculating execution time
##    total_time = end_time - start_time
##    print(result)
##    print(total_time)
