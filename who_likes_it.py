"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
items. We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. It must return the display
text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""


def likes(names):
    if not names:
        output = "no one likes this"
    elif len(names) == 1:
        output = f"{names[0]} likes this"
    elif len(names) == 2:
        output = f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        output = f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        output = f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    return output


def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


LIKES_0 = 'no one likes this'
LIKES_1 = '%s likes this'
LIKES_2 = '%s and %s like this'
LIKES_3 = '%s, %s and %s like this'
LIKES_4 = '%s, %s and %s others like this'
LIKES = {
    0: LIKES_0,
    1: LIKES_1,
    2: LIKES_2,
    3: LIKES_3,
    }


def likes3(names):
    if len(names) >= 4:
        return LIKES_4 % (names[0], names[1], len(names)-2)
    return LIKES[len(names)] % tuple(names)


if __name__ == '__main__':
    x = ["Alex", "Jacob", "Mark", "Max"]
    print(likes(x))
    print(likes2(x))
