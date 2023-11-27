import roman_number;

def test_roman_number_I():
    assert 1 == roman_number.romanNumber("I")

def test_roman_number_III():
    assert 3 == roman_number.romanNumber("III")

def test_roman_number_IV():
    assert 4 == roman_number.romanNumber("IV")

def test_roman_number_V():
    assert 5 == roman_number.romanNumber("V")

def test_roman_number_VIII():
    assert 8 == roman_number.romanNumber("VIII")

def test_roman_number_IX():
    assert 9 == roman_number.romanNumber("IX")

def test_roman_number_X():
    assert 10 == roman_number.romanNumber("X")

def test_roman_number_XL():
    assert 40 == roman_number.romanNumber("XL")

def test_roman_number_L():
    assert 50 == roman_number.romanNumber("L")

def test_roman_number_XC():
    assert 90 == roman_number.romanNumber("XC")

def test_roman_number_C():
    assert 100 == roman_number.romanNumber("C")

def test_roman_number_CCCLXIX():
    assert 369 == roman_number.romanNumber("CCCLXIX")

def test_roman_number_CD():
    assert 400 == roman_number.romanNumber("CD")

def test_roman_number_C():
    assert 500 == roman_number.romanNumber("D")

def test_roman_number_CM():
    assert 900 == roman_number.romanNumber("CM")

def test_roman_number_M():
    assert 1000 == roman_number.romanNumber("M")

def test_roman_number_MMDCCLI():
    assert 2751 == roman_number.romanNumber("MMDCCLI")
 
def test_roman_number_0():
    assert "" == roman_number.romanNumber(0)

def test_roman_number_1():
    assert "I" == roman_number.romanNumber(1)

def test_roman_number_3():
    assert "III" == roman_number.romanNumber(3)

def test_roman_number_4():
    assert "IV" == roman_number.romanNumber(4)

def test_roman_number_5():
    assert "V" == roman_number.romanNumber(5)

def test_roman_number_9():
    assert "IX" == roman_number.romanNumber(9)

def test_roman_number_10():
    assert "X" == roman_number.romanNumber(10)

def test_roman_number_40():
    assert "XL" == roman_number.romanNumber(40)

def test_roman_number_50():
    assert "L" == roman_number.romanNumber(50)

def test_roman_number_90():
    assert "XC" == roman_number.romanNumber(90)

def test_roman_number_100():
    assert "C" == roman_number.romanNumber(100)

def test_roman_number_400():
    assert "CD" == roman_number.romanNumber(400)

def test_roman_number_500():
    assert "D" == roman_number.romanNumber(500)

def test_roman_number_900():
    assert "CM" == roman_number.romanNumber(900)

def test_roman_number_1000():
    assert "M" == roman_number.romanNumber(1000)
    
def test_roman_number_2751():
    assert "MMDCCLI" == roman_number.romanNumber(2751)
