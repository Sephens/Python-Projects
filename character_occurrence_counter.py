from itertools import count
from this import s
from xml.dom.minidom import Element


def character_occurence_counter(s):
    count = {}
    for i in s:
        if i in count:
            
            count[i] +=1
        else:
            count[i] = 1
    print(count)
word = input("Enter your string: ")
print(character_occurence_counter)

    