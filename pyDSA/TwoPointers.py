from curses.ascii import isalnum
from typing import List

class TwoPointers: 

    @staticmethod 
    def isPalindrome(s: str) -> bool:
        ss=[i.lower() for i in s if i.isalnum()]
        return ss==ss[::-1]
  