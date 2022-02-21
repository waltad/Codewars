"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in
 the form of a phone number.
 Example
 create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
 """


def create_phone_number(n):
    n = [str(i) for i in n]
    return f"({''.join(n[:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"


def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number3(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"


def create_phone_number4(n):
    n = "".join([str(x) for x in n])
    return "(" + n[0:3] + ")" + " " + n[3:6] + "-" + n[6:]


def create_phone_number5(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)


create_phone_number6 = lambda n: f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(create_phone_number(array))
    print(create_phone_number2(array))
    print(create_phone_number3(array))
    print(create_phone_number4(array))
    print(create_phone_number5(array))
    print(create_phone_number6(array))
