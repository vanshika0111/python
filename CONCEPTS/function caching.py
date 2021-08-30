# function caching

"""
if a page is loaded and it takes 5 seconds
then again it was loaded, it again took 5 seconds i.e., total of 10 seconds.
Instead of loading it again & again,
store it in a container so it takes only 5 seconds
no matter how many times it was asked to load.
this is called function caching.
"""

# METHOD 1 (has delay of n seconds when called again)
import time
def some_work(n):
    # some_work takes n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Running some_work")
    some_work(3)
    print("done, calling again")
    some_work(3)
    print("called again")

# METHOD 2 (no delays when called again)
from functools import lru_cache

@lru_cache(maxsize = 3)
def some_work(n):
    # some_work takes n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Running some_work")
    some_work(3)
    print("done, calling again")
    # input()
    some_work(3)
    print("called again")
