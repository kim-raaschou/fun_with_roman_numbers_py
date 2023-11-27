import roman_numbers;

def test_roman_number_I():
    assert 1 == roman_numbers.romanNumber("I")

def test_roman_number_III():
    assert 3 == roman_numbers.romanNumber("III")

def test_roman_number_IV():
    assert 4 == roman_numbers.romanNumber("IV")

def test_roman_number_V():
    assert 5 == roman_numbers.romanNumber("V")

def test_roman_number_VIII():
    assert 8 == roman_numbers.romanNumber("VIII")

def test_roman_number_IX():
    assert 9 == roman_numbers.romanNumber("IX")

def test_roman_number_X():
    assert 10 == roman_numbers.romanNumber("X")

def test_roman_number_XL():
    assert 40 == roman_numbers.romanNumber("XL")

def test_roman_number_L():
    assert 50 == roman_numbers.romanNumber("L")

def test_roman_number_XC():
    assert 90 == roman_numbers.romanNumber("XC")

def test_roman_number_C():
    assert 100 == roman_numbers.romanNumber("C")

def test_roman_number_CCCLXIX():
    assert 369 == roman_numbers.romanNumber("CCCLXIX")

def test_roman_number_CD():
    assert 400 == roman_numbers.romanNumber("CD")

def test_roman_number_C():
    assert 500 == roman_numbers.romanNumber("D")

def test_roman_number_CM():
    assert 900 == roman_numbers.romanNumber("CM")

def test_roman_number_M():
    assert 1000 == roman_numbers.romanNumber("M")

def test_roman_number_MMDCCLI():
    assert 2751 == roman_numbers.romanNumber("MMDCCLI")
 
def test_roman_number_0():
    assert "" == roman_numbers.romanNumber(0)

def test_roman_number_1():
    assert "I" == roman_numbers.romanNumber(1)

def test_roman_number_3():
    assert "III" == roman_numbers.romanNumber(3)

def test_roman_number_4():
    assert "IV" == roman_numbers.romanNumber(4)

def test_roman_number_5():
    assert "V" == roman_numbers.romanNumber(5)

def test_roman_number_9():
    assert "IX" == roman_numbers.romanNumber(9)

def test_roman_number_10():
    assert "X" == roman_numbers.romanNumber(10)

def test_roman_number_40():
    assert "XL" == roman_numbers.romanNumber(40)

def test_roman_number_50():
    assert "L" == roman_numbers.romanNumber(50)

def test_roman_number_90():
    assert "XC" == roman_numbers.romanNumber(90)

def test_roman_number_100():
    assert "C" == roman_numbers.romanNumber(100)

def test_roman_number_400():
    assert "CD" == roman_numbers.romanNumber(400)

def test_roman_number_500():
    assert "D" == roman_numbers.romanNumber(500)

def test_roman_number_900():
    assert "CM" == roman_numbers.romanNumber(900)

def test_roman_number_1000():
    assert "M" == roman_numbers.romanNumber(1000)
    
def test_roman_number_2751():
    assert "MMDCCLI" == roman_numbers.romanNumber(2751)
