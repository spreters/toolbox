def adder(*args, **kwargs):
    num_list = []
    if args:
        for i in args:
            if not isinstance(i, (int, float)):
                print('🍎 All input must be numeric')
                return None
            num_list.append(i)

    if kwargs:
        for i in kwargs.values():
            if not isinstance(i, (int, float)):
                print('🍎 All input must be numeric')
                return None
            num_list.append(i)

    return sum(num_list)


if __name__ == '__main__':
    print(adder(1, 2.2, 3))
    print(adder(1, 2.2, 3, k=2, l=1))
    print(adder(k=1, h=2))
    print(adder())
    print(adder('ggg', 'sss'))
