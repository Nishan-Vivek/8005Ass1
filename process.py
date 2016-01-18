from multiprocessing import Pool
import time
from math import floor, sqrt

try:
    long
except NameError:
    long = int

nb_repeat = 100
tocalc =  2**59-1
f = open('process.txt', 'a')

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
    # fac(tocalc)
     f.write("%s" % fac(tocalc))


t1 = time.time()
if __name__ == '__main__':
    pool = Pool(processes=nb_repeat)
    results = pool.map(a_complex_operation, [None for _ in range(nb_repeat)])
print time.time()-t1
