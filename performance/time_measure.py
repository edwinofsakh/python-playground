import time

t11 = time.time()
t21 = time.perf_counter()
t31 = time.process_time()

time.sleep(2)

t32 = time.process_time()
t22 = time.perf_counter()
t12 = time.time()

print('time.time():\t', t12 - t11)
print('time.perf_counter():\t', t22 - t21)
print('time.process_time():\t', t32 - t31)