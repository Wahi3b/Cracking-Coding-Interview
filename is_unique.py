#Problem: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique(example):
    chars ={}
    example_list = list(example.lower())
    if example == "" :return True
    for ch in example_list:
        if ch in chars:
            return False
        else:
            chars[ch]=1
    return True
#Time complexity: takes O(1) for best case if the string is empty or the first two characters are the same, takes O(n) for worst case.

#Testing:
result = is_unique("Problematic")        
print(result)

