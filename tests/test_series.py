from math_series import __version__

from math_series.series import fibonacci

from math_series.series import lucas


def test_version():
    assert __version__ == '0.1.0'

def test_one():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected

def test_two():
	actual = insert_array([], 4)
	expected = [4]
	assert actual == expected

