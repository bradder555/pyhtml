TABLE_DATA = [
    {'a': 1,
         'b':2,
         'c':3,
         'd':4,
         'e':5,
         'f':6,
         'g':7,
         'h':8,
         'i':9,
         'j':10} for x in range(1000)]

import pyhtml

_p = pyhtml

def tmpl_src(table):
    return _p.table(
        map(lambda row:
            _p.tr(
                map(lambda column:
                    _p.td(_p.t(str(column)))
                    , row.values())
            )  # tr
            , table)
    )  # table


def test_pyhtml():
    """pyhtml template"""
    return tmpl_src(table=TABLE_DATA)()

import time

import sys
#sys.setrecursionlimit(100000)

start = time.time()
for test in range(100):
    x = test_pyhtml()
end = time.time()

avg_time = ((end - start) / 100) * 1000
print("average time: {}ms".format(avg_time))
#print(x)