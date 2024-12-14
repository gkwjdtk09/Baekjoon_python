word = input()
word_list = list(word)

CA = []
i = 0

while i < len(word_list):
    if i + 1 < len(word_list) and word_list[i] == 'c' and word_list[i+1] == '=':
        CA.append('c=')  # 'c=' 처리
        i += 2  # 두 글자를 처리했으므로 2 증가
    elif i + 1 < len(word_list) and word_list[i] == 'c' and word_list[i+1] == '-':
        CA.append('c-')  # 'c-' 처리
        i += 2
    elif i + 2 < len(word_list) and word_list[i] == 'd' and word_list[i+1] == 'z' and word_list[i+2] == '=':
        CA.append('dz=')  # 'dz=' 처리
        i += 3
    elif i + 1 < len(word_list) and word_list[i] == 'd' and word_list[i+1] == '-':
        CA.append('d-')  # 'd-' 처리
        i += 2
    elif i + 1 < len(word_list) and word_list[i] == 'l' and word_list[i+1] == 'j':
        CA.append('lj')  # 'lj' 처리
        i += 2
    elif i + 1 < len(word_list) and word_list[i] == 'n' and word_list[i+1] == 'j':
        CA.append('nj')  # 'nj' 처리
        i += 2
    elif i + 1 < len(word_list) and word_list[i] == 's' and word_list[i+1] == '=':
        CA.append('s=')  # 's=' 처리
        i += 2
    elif i + 1 < len(word_list) and word_list[i] == 'z' and word_list[i+1] == '=':
        CA.append('z=')  # 'z=' 처리
        i += 2
    else:
        CA.append(word_list[i])  # 패턴에 해당하지 않는 문자 추가
        i += 1
 
print(len(CA))
 