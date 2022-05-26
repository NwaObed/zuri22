# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #First filter out white spaces
    filterWord = word.replace(' ', '')
    filterAnagram = anagram.replace(' ', '')

    #Check if they have equal lengths
    if len(filterWord) != len(filterAnagram):
        anagram = False

    #check if they have same characters
    elif sorted(filterWord) != sorted(filterAnagram):
        anagram = False

    else:
        anagram = True


    return anagram

print(find_anagram('a gentle man','elegant man'))
print(find_anagram('Obi is a boy', 'Make python no bite you'))
print(find_anagram('restaurant ', 'runs a treat'))




