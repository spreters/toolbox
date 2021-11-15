from toolbox import calculator


## Tests on calculator()
def test_args_plus_kwargs():
    assert calculator.adder(1, 2, a=3, b=5) == 11


def test_only_args():
    assert calculator.adder(1, 2.1) == 3.1


def test_only_kwargs():
    assert calculator.adder(a=3.1, b=5) == 8.1

def test_empty_input():
    assert calculator.adder() == 0


def test_args_type():
    assert calculator.adder('ett', 'två') == None


def test_kwargs_type():
    assert calculator.adder(a='ett', b='två') == None
