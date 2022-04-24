"""Progress bars - vanilla+colorama. run in terminal"""
import math
import colorama


def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))              # pass float so we don't get weird int errors
    # █ -> alt+219
    bar = '█' * int(percent) + '-' * (100 - int(percent))  # █ for completed, - for not completed
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")           # use return carriage, print bar over same line and show %
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")   # change to green when done

# test case
numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))                              # init
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))                      # actual progress bar

print(colorama.Fore.RESET)