from collections import Counter

word = input()
word_u = word.upper()
count = Counter(word_u).most_common()
if len(count) == 1:
    print(count[0][0])
elif count[0][1] == count[1][1]: 
    print("?")
else:
    print(count[0][0])