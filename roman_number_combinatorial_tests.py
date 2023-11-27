import pytest
import roman_number

def readRomanRumberValues():
    with open("a006968.txt") as a006968:
        for lineNr, line in enumerate(a006968.readlines(), start=1):
            if lineNr <= 13 or line.strip() == "": continue
            (romanNumber, romanString) = line.split("=")
            yield (int(romanNumber.strip()), romanString.strip())


@pytest.mark.parametrize("romanNum, romanStr", readRomanRumberValues())
def test_roman_number_combinations(romanNum, romanStr):
    assert romanNum == roman_number.romanNumber(romanStr)
    assert romanStr == roman_number.romanNumber(romanNum)
    