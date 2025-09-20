import pytest
from palindrome import longest_palindromic_substring

# helper to check palindrome
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# helper to validate result
def assert_valid_result(original: str, result: str):
    assert isinstance(result, str)
    assert result in original
    assert is_palindrome(result)

# test cases
@pytest.mark.parametrize("s, valid", [
    ("babad", {"bab", "aba"}),   
    ("cbbd", {"bb"}),            
    ("a", {"a"}),                
    ("ac", {"a", "c"}),          
    ("racecar", {"racecar"}),    
    ("", {""}),                  
    ("aaaaaa", {"aaaaaa"}),      
])
def test_longest_palindromic_substring(s, valid):
    res = longest_palindromic_substring(s)
    assert_valid_result(s, res)
    assert res in valid