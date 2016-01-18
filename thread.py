from threading import Thread
import time
from math import floor, sqrt

try:
    long
except NameError:
    long = int

nb_repeat = 20
tocalc = 2**59-1

def fac(n):
    step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n // q) or [n]

def a_complex_operation(*args):
    fac(tocalc)

t1 = time.time()
threads = []
for _ in range(nb_repeat):
    threads.append(Thread(target=a_complex_operation()))

[x.start() for x in threads]
[x.join() for x in threads]
print time.time()-t1