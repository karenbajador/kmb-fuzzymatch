import multiprocessing
pool = multiprocessing.Semaphore(multiprocessing.cpu_count()) 
print(pool)