def scrabblePoints(letters_list,dic,word):
    rv = 0
    for letter in word:
        if letter in letters_list:
            rv += dic[letter]
        else:
            return -1
    return rv

def createUserName(full_name, enter_year):
    rv = ""
    last_name = full_name[full_name.find(" "):]
    return last_name[1:7] + str(enter_year)[2:] + "@someuni.edu"

def replaceFirst(word,a,b):
    pos = word.find(a)
    before = word[:pos]
    after = word[pos+1:]
    result = before+b+after
    return result

print(scrabblePoints({'a','b','c','d'}, {'a':1,'b':2,'c':3,'d':3},"abc"))
print(scrabblePoints({'a','b','c','e'}, {'a':1,'b':2,'c':3,'d':3},"afc"))
print(createUserName("ashley wang",2002))
print(createUserName("ashley wangxiaoming",2002))
print(replaceFirst("ashleyll",'l','t'))