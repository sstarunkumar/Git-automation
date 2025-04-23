# test.py
from main import longestPalindrome

assert longestPalindrome("babad") in ["bab", "aba"]
assert longestPalindrome("cbbd") == "bb"
print("Python tests passed!")
