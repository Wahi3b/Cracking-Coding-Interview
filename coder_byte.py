#The strArr contains two strings, the first one has two concatenated words, the second on has a number of words separated by a comma
#ArrayChallenge should return a string of the two words that exist in both instances of the strArr, concatenate them with the token and then replace every 3rd letter with X
def ArrayChallenge(strArr):
  first_element = strArr[0]
  second_element = strArr[1]
  second_element_words = second_element.split(',')
  token ="z1v9kt8a0e"
  for word in second_element_words:
    numberofletters = len(word)
    fisrt_element_split = first_element[:numberofletters]
    if fisrt_element_split == word:
      for word in second_element_words:
        second_element_split = first_element[numberofletters:]
        if second_element_split == word:
          return f"{fisrt_element_split},{second_element_split}{token}"
strArr = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
print(ArrayChallenge(strArr))