s = 'ab'
t = 'baab'
start_index = 0 

for elem in s:
    print(start_index)
    start_index += t[start_index:].index(elem) + 1

# def isSubsequence(s: str, t: str) -> bool:
#     sD, tD = [], []

#     for i in s: 
#         sD.append(i)

#     for j in t: 
#         if j in sD:
#            sD.pop(0)

#     print(sD, tD.reverse())

# isSubsequence("ab", "baab")
# isSubsequence("abc", "ahbgdc")
# isSubsequence("axc", "ahbgdc")
# isSubsequence("rjufvjafbxnbgriwgokdgqdqewn", 
# "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq")

# def findMaxReport(s: list) -> list:
#     updatedIndex = 0
#     maxList = []

#     for i, x in enumerate(s):
#         # if x == len(x) * x[0]: 
#             if x == s[updatedIndex+1]: 
#                 print(s[updatedIndex+1])
#                 # print(i, updatedIndex)
#                 # maxList = s[updatedIndex: i]
#                 updatedIndex = i
#                 # print("updated index", updatedIndex+1, i)
#                 # continue 
#     print (maxList) 
        
# print(findMaxReport(['yyy', 'yyy', 'yyn', 'yyn', 'yyy', 'yyy', 'yyy', 'ynn', 'yyy', 'yyy']))

# def isIsomorphic(s: str, t: str) -> bool:
#     hashmap = dict()
#     slen = len(s)
#     tlen = len(t)
#     if slen != tlen:
#         return False 

#     for i in range(slen): 
#         if s[i] in hashmap.keys(): 
#             # validate if hashmap of s is current t[index]
#             if hashmap[s[i]] in t[i]:
#                 pass
#             # reject if it is not 
#             else:
#                 return False 
#             #  if s is not in hashmap 
#         else: 
#             # immediate reject since t[index] is not s[index] 
#             if t[i] in hashmap.values():
#                 return False
#             else:
#                 hashmap[s[i]] = t[i]

#     return True

# print(isIsomorphic('egggeee','teeetst'))