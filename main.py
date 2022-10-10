import os
from decor import logger

path = os.path.join(os.getcwd(), '1.txt')

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


@logger(path)
def flat_generator(new_list):
    for item in new_list:
        for elem in item:
            yield elem


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)



