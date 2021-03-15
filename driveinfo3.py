import time
import os
from glob import glob
from pathlib import Path


directory = r"C:\\"
RUNS = 1


def run_os_walk():
    a = time.time_ns()
    for i in range(RUNS):
        fu = [x[0] for x in os.walk(directory)]
        print(fu)
    print(f"os.walk\t\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found dirs: {len(fu)}")


if __name__ == '__main__':
    run_os_walk()