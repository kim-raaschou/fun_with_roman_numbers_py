# Fun_with_roman_numbers in Python

Velkommen til "Fun With Roman Numbers" - en legende og humoristisk kode kata, hvor jeg udforsker den spændende verden af romertal i Python!

## Opgaven

Med udgangspunkt i kodekataen [Roman Numerals Kata](https://codingdojo.org/kata/RomanNumerals) har jeg udviklet en enkel implementering, der kan konvertere mellem romertal som strenge og numeriske tal.

Implementeringen er valideret op imod alle valide romertal specificeret på [The On-Line Encyclopedia of Integer Sequences® (OEIS®)](https://oeis.org/A006968/a006968.txt)

Tag en dyb indånding, og dyk ned i koden.

God fornøjelse. 

## Kode Eksempeler
```python
def test_roman_number_MMDCCLI():
    assert 2751 == roman_numbers.romanNumber("MMDCCLI")

def test_roman_number_2751():
    assert "MMDCCLI" == roman_numbers.romanNumber(2751)
