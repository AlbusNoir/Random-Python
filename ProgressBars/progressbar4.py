"""using tqdm to basically undermine the other three files"""
from tqdm import tqdm, trange
import time

for i in tqdm(range(10)):
    time.sleep(0.3)

for i in trange(10):
    time.sleep(0.3)


with tqdm(total=100) as progbar:
    for i in range(10):
        time.sleep(0.3)
        progbar.update(10)
