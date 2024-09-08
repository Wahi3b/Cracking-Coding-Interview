#Problem: Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
def check_permutation(string1,string2):
    if len(string1) != len(string2): return False
    charec1 = {}
    charec2 = {}
    first_list = list(string1)
    second_list = list(string2)
    for ch in first_list:
        if ch in charec1:
            charec1[ch] += 1
        else:
            charec1[ch] = 1
    for ch in second_list:
        if ch in charec2:
            charec2[ch] += 1
        else:
            charec2[ch] = 1
    if charec2 == charec1: return True
    else: return False
#Time complexity: Since the two strings must be in the same length, best case is O(1) is the length is not the same, worst case will be O(n+n) which is O(n)

#Testing
result = check_permutation("master","mister")
print(result)