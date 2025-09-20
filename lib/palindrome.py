#def longest_palindromic_substring(s):
#    raise NotImplementedError("Implement me after writing tests")

def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    n = len(s)
    if n == 0:
        return ""
    if n < 2:
        return s

    start = 0
    max_len = 1

    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    for i in range(n):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        best = max(len1, len2)
        if best > max_len:
            max_len = best
            start = i - (max_len - 1) // 2

    return s[start:start + max_len]