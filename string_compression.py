#String Compression: Implement a method to perform basic string compression using the counts
#of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
#"compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def str_compression(s):
    str_list = list(s)
    final_string = ""
    counter = 0
    for i,ch in enumerate(str_list):
        
        if i==0: 
            previous_ch = ch
            counter+=1
            continue

        if ch == previous_ch:
            counter+=1
        else:
            final_string+= previous_ch + str(counter)
            previous_ch=ch
            counter = 1
        if i==len(str_list)-1:
            final_string+= previous_ch + str(counter)
    return final_string
#Testing
print(str_compression('aabbbcccaaaa'))
        
        
     