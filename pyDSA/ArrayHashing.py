from typing import List

class ArrayHashing:
    
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        countS, countT = {}, {}

        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT 

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        checkMap = {} 

        for index, value in enumerate(nums):
            diff = target - value
            if diff in checkMap:
                return [checkMap[diff], index]
            checkMap[value] = index
 
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False