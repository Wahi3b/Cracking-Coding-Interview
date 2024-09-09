#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string. (Note: If implementing in Java, please use a character array so that you can
#perform this operation in place.)

def urlify(input_str,inp_len):
    filler = "%20"
    input_split = input_str.split()
    final_string = ""
    for i,word in enumerate(input_split):
        final_string +=word
        if i != inp_len-1:
            final_string += filler
    return final_string
#Time complexity: it takes O(n) n is the length of the input string

#Testing
result = urlify("Wahib Ben Said",3)
print(result)


