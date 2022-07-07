def caesarCipher(s, k):
    temp = []

    # convert char to ascii value
    for char in s:
        temp.append(ord(char))

    for i in range(len(temp)):
        # uppercase 65 - 90
        if 65 <= temp[i] <= 90:
            temp[i]= (65+(temp[i]-65+k)%26)
        elif 97 <= temp[i]<=122:
            temp[i]=(97+(temp[i]-97+k)%26)
   
    return "".join(map(chr,temp))


print(caesarCipher("A", 2))
