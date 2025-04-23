# main.py
def longestPalindrome(s):
    if not s: return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i+1)
        maxlen = max(len1, len2)
        if maxlen > end - start:
            start = i - (maxlen - 1)//2
            end = i + maxlen//2
    return s[start:end+1]

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
