"""idk man I'm on a progressbar kick right now"""
# 1 - super simple nothing fancy
for i, x in enumerate(list(range(10001))):
    print(i, end='\r')


# 2 - good ole tqdm but with more pizzazz
from tqdm import tqdm
loop = tqdm(total = 5000, position=0, leave=False)
for i in range(5000):
    loop.set_description("Loading...".format(i))
    loop.update(1)
loop.close()


# 3 - tqdm with or without pizzazz (it's more pizzazz & it's faster.)
from tqdm.auto import tqdm
for i in tqdm(range(100001)):
    print(" ", end='\r')