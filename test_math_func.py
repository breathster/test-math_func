import pytest

from math_func import minimum, maximum, add, mult, sorting
from timeit import default_timer as timer

def test_minimum():
    assert minimum(1, -3, 9, 15) == -3
    assert minimum(5, 0, 9, 15) == 0
    assert minimum(11119, 3, -0.5) == -0.5
    assert minimum(23, 15, 58) == 15


def test_minimum_letters():
    test_cases = [
        "a",
        "abba",
        "1 a"
    ]

    for x in test_cases:
        with pytest.raises(ValueError):
            minimum(x)


def test_maximum():
    assert maximum(1, 5, -7) == 5
    assert maximum(-15, -100, -0.3) == -0.3


def test_maximum_letters():
    test_cases = [
        "a12",
        "aze",
        "tt"
    ]
    for x in test_cases:
        with pytest.raises(ValueError):
            maximum(x)


def test_add():
    assert add(0, 8, 9, 1111) == 1128
    assert add(0, 0, 0) == 0
    assert add(-5, -4, 10) == 1


def test_add_letters():
    test_cases = [
        "a12",
        "aze",
        "tt"
    ]
    for x in test_cases:
        with pytest.raises(ValueError):
            add(x)


def test_mult():
    assert mult(-3, -3, 2) == 18
    assert mult(0, 5, 1) == 0


def test_mult_letters():
    test_cases = [
        "a12",
        "aze",
        "tt"
    ]
    for x in test_cases:
        with pytest.raises(ValueError):
            mult(x)


def test_mult_too_much_numbers():
    test_cases = [15, 3, 81, 41, 62, 142, 105, 1, 92, 77, 95, 46, 27, 35, 59, 76, 47, 100, 123, 98, 37, 22, 115, 42, 25, 68, 119, 80, 138, 126, 129, 144, 94, 65, 102, 122, 54, 103, 78, 139, 14, 30, 72, 64, 124, 118, 50, 146, 36, 99, 93, 113, 31, 29, 32, 107, 91, 148, 74, 106, 147, 63, 51, 75, 45, 137, 43, 86, 108, 80, 138, 126, 129, 144, 94, 65, 102, 122, 54, 103, 78, 139, 14, 30, 72, 64, 124, 118, 50, 146, 36, 99, 93, 113, 31, 29, 32, 107, 91, 148, 74, 106, 147, 63, 51, 75, 45, 137, 43, 86, 108, 136, 16, 120, 56, 83, 57, 134, 58, 21, 33, 48, 71, 112, 73, 53, 111, 61, 150, 130, 17, 3, 60, 131, 69, 7, 4, 143, 116, 70, 15, 87, 8, 6, 149, 97, 39, 135, 67, 145, 28, 66, 11, 82, 88, 127, 90, 140, 13, 24, 10, 55, 121, 2, 5, 141, 104, 23, 125, 20, 85, 40, 132, 89, 109, 96, 114, 49, 34, 26, 44, 52, 133, 128, 117, 12, 110, 84, 9, 19, 79, 101, 38]
    with pytest.raises(ValueError):
        mult(test_cases)


def test_mult_too_big_numbers():
    test_cases = [100000, 99999999, 150000000, 50000000000]
    with pytest.raises(ValueError):
        mult(test_cases)


def test_sorting():
    assert sorting(0, 8, 9, 1111) == [0, 8, 9, 1111]
    assert sorting(15, 59, 98, -3, 0.5) == [-3, 0.5, 15, 59, 98]


def test_sorting_letters():
    test_cases = [
        "a12",
        "aze",
        "tt"
    ]
    for x in test_cases:
        with pytest.raises(ValueError):
            sorting(x)


def time_testing():
    start1 = timer()
    test_case1 = [1, -3, 9, 15, 19, 0.5]
    min1 = minimum(test_case1)
    max1 = maximum(test_case1)
    add1 = add(test_case1)
    mult1 = mult(test_case1)
    sorting1 = sorting(test_case1)
    end1 = timer()
    dur1 = end1 - start1
    start2 = timer()
    test_case2 = [1, -3, 9, 15, 19, 0.5, 133, 27, 77, 102, 131, 26, 91, 51, 146, 3, 118, 48, 101, 42, 137, 129, 0.3, -10]
    min2 = minimum(test_case1)
    max2 = maximum(test_case1)
    add2 = add(test_case1)
    mult2 = mult(test_case1)
    sorting2 = sorting(test_case1)
    end2 = timer()
    dur2 = end2 - start2
    assert dur2 <= dur1 * 4