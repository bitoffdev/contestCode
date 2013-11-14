method, text = raw_input().split()
headers = ["A", "D", "F", "G", "V", "X"]
cipher = ["PH0QG6", "4MEA1Y", "L2NOFD", "XKR3CV", "S5ZW7B", "J9UTI8"]
output=""
if method=="1":
    for letter in text:
        for row in cipher:
            for item in row:
                if item==letter:
                    output+=headers[cipher.index(row)]+headers[row.index(item)]
elif method=="2":
    i=0
    while i<len(text):
        row=headers.index(text[i])
        i+=1
        col=headers.index(text[i])
        i+=1
        output+=cipher[row][col]
print output
