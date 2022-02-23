"""In this little assignment you are given a string of space separated numbers, and have to return the highest and
lowest number.
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""


def high_and_low(string):
    array = [int(n) for n in list(string.split())]
    return f"{max(array)} {min(array)}"


def high_and_low2(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))


def high_and_low3(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])


if __name__ == '__main__':
    x = "1 2 -3 4 5"
    print(high_and_low(x))
