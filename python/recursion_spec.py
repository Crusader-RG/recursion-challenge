import pytest
from recursion_challenge import factorial
from recursion_challenge import palindrome
from recursion_challenge import bottles
from recursion_challenge import roman_num

def test_recursion_challenge():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(13) == 6227020800

@pytest.mark.parametrize("num, expected_output", [
    (3, "3 bottles\n2 bottles\n1 bottle\nno bottles\n"),
    (4, "4 bottles\n3 bottles\n2 bottles\n1 bottle\nno bottles\n")
])
def test_bottles(capfd, num, expected_output):
    bottles(num)
    captured = capfd.readouterr()
    assert captured.out == expected_output

def test_palindrome():
    assert palindrome("racecar") == True
    assert palindrome('justin') == False
    assert palindrome('pv1vp') == True
    assert palindrome('1234321') == True

def test_roman_num():
    assert roman_num(3) == "III"
    assert roman_num(10) == "X"
    assert roman_num(27) == "XXVII"
    assert roman_num(49) == "XLIX"