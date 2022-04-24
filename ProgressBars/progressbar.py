"""Progress bars - vanilla. run in actual cmd or terminal"""
import math


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))              # pass float so we don't get weird int errors
    # █ -> alt+219
    bar = '█' * int(percent) + '-' * (100 - int(percent))  # █ for completed, - for not completed
    print(f"\r|{bar}| {percent:.2f}%", end="\r")           # use return carriage, print bar over same line and show %


# test case
numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))                              # init
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))                      # actual progress bar