word = input()
length = int(len(word)/2)

for i in range(0, length+1):
    if word[i] == word[-(i+1)]:
        result = 1
    else:
        result = 0
        break
print(result)